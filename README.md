# AI-Based Automotive Visual Inspection & Quality Control System

An experimental computer-vision application that analyzes vehicle or
car-part images and highlights potential damage using a trained YOLO
model. The Streamlit interface displays predicted damage labels,
confidence scores, annotated images, and downloadable CSV inspection
reports.

> **Important:** This is a prototype, not a certified automotive
> inspection system. The current model has low detection performance and
> may miss visible damage or produce false detections. Every result must
> be checked by a qualified human inspector. Do not use this application
> as the sole basis for safety, repair, or quality-control decisions.

## 🚀 Live Demo

**Streamlit App:** `ADD_YOUR_STREAMLIT_APP_URL_HERE`

After deployment, replace the placeholder above with the public
Streamlit Community Cloud URL. Visitors will then be able to open the
app in their browser.

## 📌 Project Overview

Automotive inspection can involve reviewing images for visible damage
such as dents, scratches, corrosion, cracks, paint chips, and missing or
broken parts. This project explores how computer vision can support that
review process.

The application lets a user upload an image, run model inference,
inspect predicted detections, and download the results as a CSV file for
further review. The prediction output is intended to support---not
replace---human inspection.

## 🎯 Project Objectives

-   Build a simple browser-based interface for image inspection.
-   Apply a trained YOLO model to uploaded automotive images.
-   Display predicted damage categories and confidence scores.
-   Show annotated images with detection boxes.
-   Present detection details in a table.
-   Export inspection information as a CSV report.
-   Make the prototype accessible through Streamlit Community Cloud.

## ✨ Key Features

-   **Image upload:** Upload a supported vehicle or car-part image.
-   **Damage detection:** Run the trained model on the uploaded image.
-   **Visual results:** Display the image with predicted detections.
-   **Confidence scores:** Review the model's confidence for each
    prediction.
-   **Detection table:** Review the predicted class and associated
    details.
-   **Inspection metadata:** Record available inspection information in
    the app.
-   **CSV export:** Download inspection results for record-keeping and
    human review.
-   **Human-review reminder:** Results are not treated as a certified
    pass/fail decision.

## 🧩 Damage Categories

The model was trained with these eight damage categories:

1.  Broken part
2.  Corrosion
3.  Cracked
4.  Dent
5.  Flaking
6.  Missing part
7.  Paint chip
8.  Scratch

A prediction indicates what the model detected in an image; it does not
confirm that the vehicle has that defect.

## 🖥️ Application Output

The screenshots below are intended to show example application outputs.
Copy your actual screenshots into the `Inspection Report` folder and
rename them to match these paths, or update the paths in this README to
match your filenames.

### Example 1 --- Damage detection

![Automotive inspection output 1](Inspection%20Report/output_1.png)

### Example 2 --- Detection results

![Automotive inspection output 2](Inspection%20Report/output_2.png)

### Example 3 --- Annotated vehicle image

![Automotive inspection output 3](Inspection%20Report/output_3.png)

### Example 4 --- Additional inspection result

![Automotive inspection output 4](Inspection%20Report/output_4.png)

### Example 5 --- Additional inspection result

![Automotive inspection output 5](Inspection%20Report/output_5.png)

> GitHub displays images only when the referenced files are committed to
> the repository at the specified paths. Replace these example paths
> with the exact filenames of your saved screenshots if needed. Use
> screenshots that accurately represent the application; do not present
> selected detections as proof of high overall accuracy.

## 📄 CSV Inspection Reports

The app can export inspection results as CSV files. Add your actual
exported CSV reports to `Inspection Report/` and list the filenames
below.

  -----------------------------------------------------------------------
  Report                              Description
  ----------------------------------- -----------------------------------
  `inspection_report_1.csv`           Example CSV report for an inspected
                                      image

  `inspection_report_2.csv`           Example CSV report for another
                                      image

  `inspection_report_3.csv`           Example CSV report for another
                                      image
  -----------------------------------------------------------------------

The filenames above are examples. Rename the links to match the actual
CSV reports you upload.

-   [Open CSV report 1](Inspection%20Report/inspection_report_1.csv)
-   [Open CSV report 2](Inspection%20Report/inspection_report_2.csv)
-   [Open CSV report 3](Inspection%20Report/inspection_report_3.csv)

CSV files contain model-generated results and should be reviewed
alongside the original image. A CSV report does not independently verify
whether a detected defect is real.

## 🧠 Model and Dataset

The model was trained using the public **Car Parts and Car Damages
Dataset** from Humans in the Loop:

-   Dataset page:
    https://humansintheloop.org/resources/datasets/car-parts-and-car-damages-dataset/
-   Dataset license stated by the project notes: CC0

The training workflow used a damage-only dataset with eight target
classes and a YOLO segmentation model. The trained weights used by the
app are stored in `best.pt`.

### Reported test results

The final test evaluation for the current model was:

  Metric         Box result   Mask result
  ------------ ------------ -------------
  Precision          18.42%        18.95%
  Recall             14.03%        11.84%
  mAP@50             10.76%         9.13%
  mAP@50--95          5.61%         4.08%

These results indicate that the model is currently experimental and not
reliable enough for independent real-world inspection. It may miss
defects and may also generate incorrect or overlapping detections.
Improving dataset quality, annotation consistency, class balance, and
training/evaluation is a future task.

## ⚙️ Technology Stack

  Technology                  Purpose
  --------------------------- -------------------------------------------
  Python                      Application and inference logic
  Streamlit                   Web interface
  Ultralytics YOLO            Object detection / segmentation inference
  PyTorch                     Model runtime
  Pillow                      Image handling
  Pandas                      Tabular data and CSV reporting
  Git and GitHub              Version control and source hosting
  Streamlit Community Cloud   Planned public deployment

## 📁 Project Structure

``` text
Automotive_Inspection/
├── app.py
├── best.pt
├── requirements.txt
├── README.md
└── Inspection Report/
    ├── output_1.png
    ├── output_2.png
    ├── output_3.png
    ├── output_4.png
    ├── output_5.png
    ├── inspection_report_1.csv
    ├── inspection_report_2.csv
    └── inspection_report_3.csv
```

The screenshot and CSV names shown above are suggested examples. Keep
your actual filenames or rename the README references accordingly. The
original `Dataset/` folder is intentionally not shown here; it is
usually better not to upload the entire dataset to GitHub when the app
only needs the trained model and application files.

### File responsibilities

-   `app.py` --- Streamlit user interface, inference, result display,
    and report export.
-   `best.pt` --- trained model weights loaded by the application.
-   `requirements.txt` --- Python package dependencies.
-   `Inspection Report/` --- selected output screenshots and sample CSV
    reports.
-   `README.md` --- project documentation.

## 🛠️ Run Locally

### 1. Clone the repository

Replace the URL if your repository name differs:

``` bash
git clone https://github.com/ar-rohit01/Automotive_Inspection.git
cd Automotive_Inspection
```

### 2. Create and activate a virtual environment (recommended)

**Windows:**

``` bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Start Streamlit

``` bash
python -m streamlit run app.py
```

Open the local URL shown in the terminal, usually
`http://localhost:8501`.

## ☁️ Deployment on Streamlit Community Cloud

The deployment process requires a GitHub repository containing the
application source, dependency file, and model weights.

1.  Push the project files to the GitHub repository.
2.  Open https://share.streamlit.io/.
3.  Choose **Create app** / **Deploy an app**.
4.  Select the `Automotive_Inspection` repository and its branch.
5.  Set the app entry point to `app.py`.
6.  Deploy and wait for the build to complete.
7.  Test the live app by uploading a sample image.
8.  Replace `ADD_YOUR_STREAMLIT_APP_URL_HERE` above with the final app
    URL.

Deployment can fail if dependency versions are unavailable or
incompatible. If that happens, review the Streamlit build logs and
update `requirements.txt` based on the error.

## 🔍 Typical Workflow

``` text
Upload vehicle/car-part image
            ↓
Choose inspection settings
            ↓
Run model inference
            ↓
View annotated image and predicted labels
            ↓
Review confidence scores and detection table
            ↓
Download CSV report
            ↓
Human inspector reviews the original image and predictions
```

## ⚠️ Limitations and Responsible Use

-   The current test metrics are low, so predictions are not dependable
    enough for standalone use.
-   The model may miss real damage, produce false positives, or place
    overlapping boxes.
-   Confidence scores are model outputs, not probabilities that a defect
    definitely exists.
-   Image quality, lighting, viewpoint, and damage appearance may affect
    results.
-   This prototype does not certify a vehicle as safe, damaged, or
    repair-ready.
-   A human inspector must verify every result against the original
    image.
-   Do not upload private, sensitive, or confidential images without
    permission.

## 🔮 Future Improvements

-   Improve annotation quality and dataset balance.
-   Collect more representative images for each damage category.
-   Tune training parameters and evaluate alternatives.
-   Measure per-class precision, recall, and mAP on a held-out test set.
-   Reduce false positives and overlapping detections.
-   Improve localization and display of predicted damage.
-   Add clearer inspection history and report management.
-   Add a human-confirmed status field separate from model predictions.
-   Improve deployment dependency management and error handling.

## 👨‍💻 Author

**Rohit Rajaram Yadav**\
B.Tech --- Automation & Robotics Engineering

### Connect with me

-   **LinkedIn:** https://www.linkedin.com/in/rohit-yadav-6b8999299/
-   **GitHub profile:** https://github.com/ar-rohit01
-   **Project repository:**
    https://github.com/ar-rohit01/Automotive_Inspection
-   **Streamlit app:** `ADD_YOUR_STREAMLIT_APP_URL_HERE`

## 📌 Project Summary

The AI-Based Automotive Visual Inspection & Quality Control System is a
computer-vision prototype that applies a trained YOLO model to
automotive images and presents predicted damage detections through a
Streamlit interface. It includes annotated visual outputs and CSV export
to support human review. The model's current performance is limited, and
further data, training, and evaluation work is required before it could
be considered for practical inspection use.
