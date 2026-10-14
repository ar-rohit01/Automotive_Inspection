# 🚗 Automotive Visual Inspection System

An end-to-end, AI-powered computer vision application built with **YOLO object detection** and **Streamlit** for automated vehicle body damage detection and inspection reporting.

---

## 🚀 Project Overview

Vehicle body inspections often involve manually identifying and logging damages from photographs. This process can be time-consuming and inconsistent.
This project provides an automated AI-powered solution that analyzes vehicle images, detects surface defects using custom bounding boxes, and exports detailed inspection logs.

The application detects:
🛠️ Surface Damage Classes (Broken parts, corrosion, cracks, dents, flaking, missing parts, paint chips, and scratches)
📊 Inspection Metrics (Confidence scores, bounding box coordinates, timestamps, and unique inspection IDs)

---

## 🎯 Problem Statement

Manual automotive visual inspections lack real-time standardization and automated data tracking. 
By leveraging a trained YOLO object detection model coupled with a Streamlit interface, inspectors can instantly process vehicle photos and generate clean visual reports and CSV data logs.

---

## 🎯 Project Objectives

The main objectives of this project are:
- Automatically detect vehicle body damages using YOLO.
- Provide a clean and adjustable Streamlit user interface.
- Allow users to select specific vehicle models (e.g., Tata Curvv, Tata Nexon, Tata Punch).
- Configure confidence thresholds and NMS IoU suppression.
- Generate and export structured CSV inspection reports.
- Prepare the application for cloud deployment.

---

## 🧠 Solution Approach

The application follows a streamlined computer vision pipeline:
```text
                USER
                  │
                  ▼
        ┌──────────────────┐
        │  Streamlit UI    │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ YOLO Model (pt)  │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Bounding Boxes   │
        │ & Class Filtering│
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ CSV Report &     │
        │ Data Export      │
        └──────────────────┘
```

---

## ✨ Key Features

### 🔹 Damage Detection
Detects 8 distinct types of automotive exterior damage:
- Broken part
- Corrosion
- Cracked
- Dent
- Flaking
- Missing part
- Paint chip
- Scratch

### 🔹 Interactive Controls
- Sidebar controls for inspector name, vehicle model selection, confidence threshold adjustment, and IoU threshold tuning.

### 🔹 Clean Bounding Box Visualization
- Uses tight window bounding boxes, class-based HSV color coding, and text labels for clear review.

### 🔹 Automated CSV Reporting
- Automatically logs inspection details and allows users to download CSV reports containing bounding box coordinates and review statuses.

---

## 🧪 Testing & Sample Outputs

The application was tested using multiple sample images and generates visual outputs alongside CSV reports.

### Sample Test Images (Stored in `Inspection Report`)
- `Car damages 14..png`
- `Car damages 103.png`
- `Car damages 111.png`
- `Car damages 116.png`
- `Car damages 172.png`
- `Car damages 256.png`
- `Car damages 864.png`

### Exported CSV Reports
- `inspection_Car damages 14..csv`
- `inspection_Car damages 103.csv`
- `inspection_Car damages 111.csv`
- `inspection_Car damages 116.csv`
- `inspection_Car damages 172.csv`
- `inspection_Car damages 256.csv`
- `inspection_Car damages 864.csv`

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core application development |
| **Ultralytics YOLO** | Object detection model framework (`best.pt`) |
| **Streamlit** | Web application user interface |
| **OpenCV & Pillow** | Image processing and bounding box rendering |
| **Pandas & NumPy** | Data manipulation and CSV report generation |
| **Git & GitHub** | Version control and repository hosting |

---

## 📁 Project Structure

```text
Automotive_Inspection/
│
├── app.py                      # Main Streamlit Web Application
├── best.pt                     # Trained YOLO Model Weights (~5.8 MB)
├── requirements.txt            # Python Dependencies
├── .gitattributes              # Git Configuration
│
└── Inspection Report/          # Sample Detection Outputs & CSV Logs
    ├── Car damages 14..png
    ├── inspection_Car damages 14..csv
    ├── Car damages 103.png
    ├── inspection_Car damages 103.csv
    └── ...
```

---

## ⚙️ Installation & Local Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ar-rohit01/Automotive_Inspection.git
   cd Automotive_Inspection
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the Environment**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **Linux / macOS:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

---

## ☁️ Deployment & Live App

The application is fully configured and deployed on **Streamlit Community Cloud**:
- **Live Web App:** [https://ar-rohit01-automotive-inspection.streamlit.app](https://ar-rohit01-automotive-inspection.streamlit.app) *(Replace with your exact Streamlit cloud URL once deployed)*

---

## 💡 Why This Project?

This project demonstrates practical implementation of several important computer vision and web development concepts:
- Object Detection with YOLO
- Custom Bounding Box Processing & HSV Color Mapping
- Streamlit Application Development
- Dynamic CSV Data Exporting
- Modular Python Architecture
- Git/GitHub Workflow & Cloud Deployment

---

## 👨‍💻 Author

**Rohit Rajaram Yadav**

* **B.Tech** — Automation & Robotics Engineering
* **Areas of Interest:** Artificial Intelligence, Machine Learning, Computer Vision, Generative AI, Intelligent Automation
* **LinkedIn:** [https://www.linkedin.com/in/rohit-yadav-6b8999299](https://www.linkedin.com/in/rohit-yadav-6b8999299)
* **GitHub:** [https://github.com/ar-rohit01](https://github.com/ar-rohit01)

⭐ **Project Repository:** [Automotive_Inspection](https://github.com/ar-rohit01/Automotive_Inspection)