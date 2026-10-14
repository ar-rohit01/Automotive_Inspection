import streamlit as st
from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
from pathlib import Path
from datetime import datetime
import uuid
import colorsys

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Automotive Visual Inspection",
    page_icon="🚗",
    layout="wide"
)

MODEL_PATH = Path(__file__).parent / "best.pt"

DAMAGE_NAMES = {
    0: "Broken part",
    1: "Corrosion",
    2: "Cracked",
    3: "Dent",
    4: "Flaking",
    5: "Missing part",
    6: "Paint chip",
    7: "Scratch"
}


# ---------------- MODEL ----------------
@st.cache_resource
def load_model():
    return YOLO(str(MODEL_PATH))


def get_font(size=18):
    """Load a readable font, with a safe fallback."""
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


def draw_clean_detections(image, result, detections):
    """
    Draw tight, compact bounding boxes around detected defects,
    clamping down overly stretched boxes to highlight only the local defect zone.
    """
    output = image.copy().convert("RGB")
    draw = ImageDraw.Draw(output)
    font = get_font(max(14, min(output.width, output.height) // 35))
    line_width = max(2, min(output.width, output.height) // 300)

    boxes = result.boxes
    if boxes is None or len(boxes) == 0:
        return output

    # Assign a consistent color per class.
    class_colors = {}
    for item in detections:
        class_id = item["Class ID"]
        if class_id not in class_colors:
            hue = (class_id * 0.137 + 0.02) % 1.0
            rgb = colorsys.hsv_to_rgb(hue, 0.85, 0.95)
            class_colors[class_id] = tuple(int(c * 255) for c in rgb)

    # Sort high-confidence detections first so they are drawn on top.
    box_items = []
    for box in boxes:
        class_id = int(box.cls.item())
        score = float(box.conf.item())
        xyxy = box.xyxy[0].tolist()
        box_items.append((score, class_id, xyxy))

    box_items.sort(reverse=True, key=lambda x: x[0])

    for score, class_id, xyxy in box_items:
        x1, y1, x2, y2 = [int(round(v)) for v in xyxy]
        
        # Enforce strict tightness: if a box height stretches disproportionately
        # relative to its width, condense it into a compact local window around the center.
        width = x2 - x1
        height = y2 - y1
        if height > width * 1.8:
            center_y = (y1 + y2) // 2
            target_height = int(width * 1.4)
            y1 = max(0, center_y - target_height // 2)
            y2 = min(output.height, center_y + target_height // 2)

        color = class_colors.get(class_id, (255, 180, 0))
        label = f"{DAMAGE_NAMES.get(class_id, f'Class {class_id}')} {score:.2f}"

        draw.rectangle(
            [x1, y1, x2, y2],
            outline=color,
            width=line_width
        )

        # Label background kept inside the image bounds.
        text_bbox = draw.textbbox((0, 0), label, font=font)
        text_w = text_bbox[2] - text_bbox[0]
        text_h = text_bbox[3] - text_bbox[1]
        label_y = max(0, y1 - text_h - 6)
        label_x = max(0, min(x1, output.width - text_w - 8))

        draw.rectangle(
            [label_x, label_y, label_x + text_w + 8, label_y + text_h + 4],
            fill=color
        )
        draw.text(
            (label_x + 4, label_y + 2),
            label,
            fill=(15, 15, 15),
            font=font
        )

    return output


# ---------------- HEADER ----------------
st.title("🚗 Automotive Visual Inspection System")
st.caption("AI-based vehicle damage detection prototype")

st.warning(
    "Experimental prototype: model accuracy is limited. Predictions are not "
    "certified inspection results and must not be used alone for safety, "
    "repair, insurance, or pass/fail decisions."
)

if not MODEL_PATH.exists():
    st.error(f"Model file not found: {MODEL_PATH}")
    st.stop()

try:
    model = load_model()
except Exception as error:
    st.error(f"Could not load the model: {error}")
    st.stop()


# ---------------- SIDEBAR ----------------
st.sidebar.header("Inspection Details")

vehicle_model = st.sidebar.selectbox(
    "Vehicle model",
    ["Tata Curvv", "Tata Nexon", "Tata Punch", "Other / Unknown"]
)
inspector = st.sidebar.text_input("Inspector name (optional)")

confidence = st.sidebar.slider(
    "Minimum confidence threshold",
    min_value=0.05,
    max_value=0.90,
    value=0.25,
    step=0.05,
    help="Raising this hides lower-confidence detections; it can also hide real damage."
)

iou_threshold = st.sidebar.slider(
    "Overlap suppression (IoU)",
    min_value=0.10,
    max_value=0.80,
    value=0.45,
    step=0.05,
    help="Controls suppression of overlapping predictions of the same class."
)

st.sidebar.caption("Inference device: CPU")


# ---------------- UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload a vehicle image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")
    except Exception:
        st.error("The uploaded file could not be opened as an image.")
        st.stop()

    st.subheader("Uploaded Image")
    st.image(image, caption=uploaded_file.name, use_container_width=True)

    if st.button("🔍 Run Damage Inspection", type="primary"):
        with st.spinner("Analyzing image..."):
            try:
                results = model.predict(
                    source=image,
                    conf=confidence,
                    iou=iou_threshold,
                    imgsz=640,
                    device="cpu",
                    verbose=False
                )
            except Exception as error:
                st.error(f"Prediction failed: {error}")
                st.stop()

        result = results[0]
        detections = []
        boxes = result.boxes

        if boxes is not None and len(boxes) > 0:
            for box in boxes:
                class_id = int(box.cls.item())
                score = float(box.conf.item())
                x1, y1, x2, y2 = [
                    round(float(value), 1)
                    for value in box.xyxy[0].tolist()
                ]
                detections.append({
                    "Damage": DAMAGE_NAMES.get(class_id, f"Unknown class {class_id}"),
                    "Confidence (%)": round(score * 100, 2),
                    "Class ID": class_id,
                    "X1": x1,
                    "Y1": y1,
                    "X2": x2,
                    "Y2": y2
                })

        # ---------------- RESULTS ----------------
        st.divider()
        st.subheader("Inspection Results")

        col1, col2, col3 = st.columns(3)
        col1.metric("Detected instances", len(detections))
        col2.metric(
            "Damage categories",
            len(set(item["Damage"] for item in detections))
        )
        col3.metric("Vehicle model", vehicle_model)

        st.markdown("### Clear Detection View")
        if detections:
            clean_image = draw_clean_detections(image, result, detections)
            st.image(
                clean_image,
                caption="Compact bounding-box view; predictions still require human verification",
                use_container_width=True
            )
        else:
            st.image(image, caption="No detections shown", use_container_width=True)
            st.info(
                "No damage was detected at this threshold. This does not mean "
                "the vehicle is defect-free."
            )

        if detections:
            display_df = pd.DataFrame([
                {
                    "Damage": item["Damage"],
                    "Confidence (%)": item["Confidence (%)"],
                    "Bounding box (x1, y1, x2, y2)": (
                        f"({item['X1']}, {item['Y1']}, "
                        f"{item['X2']}, {item['Y2']})"
                    )
                }
                for item in detections
            ])
            st.markdown("### Detection Details")
            st.dataframe(display_df, use_container_width=True, hide_index=True)

        # ---------------- REPORT ----------------
        inspection_id = str(uuid.uuid4())[:8].upper()
        inspection_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        inspector_name = inspector.strip() or "Not specified"

        st.divider()
        st.subheader("Inspection Report")
        st.write(f"**Inspection ID:** {inspection_id}")
        st.write(f"**Date and time:** {inspection_time}")
        st.write(f"**Image filename:** {uploaded_file.name}")
        st.write(f"**Vehicle model:** {vehicle_model}")
        st.write(f"**Inspector:** {inspector_name}")
        st.write("**Decision:** Requires human review; no automated pass/fail decision.")

        report_df = pd.DataFrame(detections)
        if report_df.empty:
            report_df = pd.DataFrame(
                columns=[
                    "Damage", "Confidence (%)", "Class ID",
                    "X1", "Y1", "X2", "Y2"
                ]
            )

        report_df.insert(0, "Inspection ID", inspection_id)
        report_df.insert(1, "Date and time", inspection_time)
        report_df.insert(2, "Image filename", uploaded_file.name)
        report_df.insert(3, "Vehicle model", vehicle_model)
        report_df.insert(4, "Inspector", inspector_name)
        report_df["Review status"] = "Requires human review"

        st.download_button(
            "📥 Download Inspection Report (CSV)",
            data=report_df.to_csv(index=False).encode("utf-8"),
            file_name=f"inspection_{inspection_id}.csv",
            mime="text/csv"
        )

st.divider()
st.caption(
    "Model trained on a public car-damage dataset. Predictions may be inaccurate "
    "or incomplete. This display change improves readability only; it does not "
    "improve the model's underlying accuracy. A qualified human inspector must "
    "verify findings."
)