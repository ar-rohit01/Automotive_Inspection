# AI-Based Automotive Visual Inspection & Quality Control System

**Author:** Rohit Rajaram Yadav  
**Domain:** Artificial Intelligence, Computer Vision & Automotive Quality Inspection  
**Education:** B.Tech — Automation & Robotics Engineering

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![YOLO](https://img.shields.io/badge/YOLO-Object%20Detection-purple)](https://docs.ultralytics.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?logo=pytorch)](https://pytorch.org/)

## 1. Project Overview

The **AI-Based Automotive Visual Inspection & Quality Control System** is an experimental computer-vision project designed to detect visible damage on vehicle images using a trained YOLO-based model.

The application provides a Streamlit interface where users can upload a vehicle image, view predicted damage detections, review confidence scores, and download a CSV inspection report.

The project demonstrates how computer vision and deep learning can be applied to automotive visual inspection workflows.

**Important:** This is an educational prototype. The current model has low detection performance and requires further training and validation before it could be considered for practical inspection use.

## 2. Project Objectives

- Develop an AI-based prototype for automotive damage detection.
- Apply a trained YOLO model to uploaded vehicle images.
- Display predicted damage labels, confidence scores, and bounding boxes.
- Generate downloadable CSV inspection reports.
- Explore the application of computer vision in automotive quality control.
- Identify areas for improvement in model accuracy and reliability.

## 3. Damage Categories

The model was trained to detect the following eight damage categories:

| Class ID | Damage Category |
|---:|---|
| 0 | Broken part |
| 1 | Corrosion |
| 2 | Cracked |
| 3 | Dent |
| 4 | Flaking |
| 5 | Missing part |
| 6 | Paint chip |
| 7 | Scratch |

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application programming |
| Streamlit | Interactive web interface |
| Ultralytics YOLO | Object detection and segmentation |
| PyTorch | Deep learning framework |
| Pillow | Image handling |
| Pandas | Inspection data and CSV reports |
| Git and GitHub | Version control and project hosting |
| Streamlit Community Cloud | Intended web deployment platform |

## 5. Model Evaluation Results

The following results are from the recorded test evaluation of the current trained model.

### Bounding-box metrics

| Metric | Result |
|---|---:|
| Precision | 18.42% |
| Recall | 14.03% |
| mAP@50 | 10.76% |
| mAP@50–95 | 5.61% |

### Segmentation-mask metrics

| Metric | Result |
|---|---:|
| Precision | 18.95% |
| Recall | 11.84% |
| mAP@50 | 9.13% |
| mAP@50–95 | 4.08% |

### Interpretation

These results indicate that the current model has limited damage-detection performance. It may miss visible damage, produce false-positive detections, or identify damage incorrectly.

The model should be treated as an experimental prototype. All predictions require human verification, and the results should not be interpreted as proof that a vehicle is safe or free from damage.

## 6. Application Features

- Upload vehicle images in JPG, JPEG, or PNG format.
- Select a vehicle model in the application.
- Enter inspector information.
- Adjust confidence and IoU thresholds.
- Run the trained model on an uploaded image.
- View annotated images with predicted damage labels.
- Review confidence scores and detection details.
- View predicted bounding-box coordinates.
- Download CSV inspection reports.
- Record inspection metadata and review status.

## 7. Project Structure

```text
Automotive_Inspection/
│
├── app.py
├── best.pt
├── requirements.txt
│
├── Dataset/
│
├── Inspection Report/
│   ├── Car damages 4.png
│   ├── Car damages 103.png
│   ├── Car damages 11.png
│   ├── Car damages 152.png
│   ├── Car damages 72.png
│   ├── Car damages 255.png
│   ├── Car damages 85/1.png
│   ├── inspection report CSV files
│   └── other inspection outputs
│
└── README.md
```

*Note: The names and subfolder structure above are illustrative based on the supplied report-folder listing. Keep the actual filenames and paths from your project when organizing the repository.*

## 8. Installation and Local Execution

### Prerequisites

- Python installed on your computer.
- Git, if you plan to publish the project on GitHub.
- The project files, including `app.py`, `best.pt`, and `requirements.txt`.

### Step 1: Open the project folder

Open a terminal in the project directory:

```bash
cd D:\Automotive_Inspection
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Start the Streamlit application

```bash
python -m streamlit run app.py
```

### Step 4: Open the application

Open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

Upload an image to view the model's predictions and available inspection-report information.

## 9. Inspection Output Examples

The images below are intended to show example outputs from the current application. The image paths must match the actual filenames committed to the GitHub repository.

If your files are in the `Inspection Report` folder, use their exact relative paths. For example:

```markdown
![Inspection output](Inspection%20Report/Car%20damages%204.png)
```

To display an image directly on GitHub, the path in the Markdown must match the committed filename and folder structure.

### Example inspection images

Add the following image references after confirming the exact paths:

```markdown
![Inspection output 1](Inspection%20Report/Car%20damages%204.png)

![Inspection output 2](Inspection%20Report/Car%20damages%20103.png)

![Inspection output 3](Inspection%20Report/Car%20damages%2011.png)

![Inspection output 4](Inspection%20Report/Car%20damages%20152.png)

![Inspection output 5](Inspection%20Report/Car%20damages%2072.png)

![Inspection output 6](Inspection%20Report/Car%20damages%20255.png)
```

Verify each filename before using these references. If an image is stored in a subfolder, include that subfolder in the path.

## 10. CSV Inspection Reports

The application can generate downloadable CSV reports containing inspection metadata and predicted detections.

Depending on the report produced by the application, the information may include:

- Inspection ID
- Inspection date and time
- Source image filename
- Selected vehicle model
- Inspector name
- Predicted damage category
- Confidence score
- Class ID
- Bounding-box coordinates
- Human-review status

To make a report accessible from GitHub, commit the CSV file to the repository and link it using its exact relative path.

Example Markdown:

```markdown
[View inspection report](Inspection%20Report/your_actual_report.csv)
```

Replace `your_actual_report.csv` with the real CSV filename.

## 11. Dataset and Attribution

The project uses the public **Car Parts and Car Damages Dataset** from Humans in the Loop.

Dataset source:

https://humansintheloop.org/resources/datasets/car-parts-and-car-damages-dataset/

The dataset source describes the dataset as CC0. Review the source page for the dataset's details and terms.

## 12. Limitations and Responsible Use

- The current model has low precision, recall, and mAP scores.
- Predictions can include false positives, missed damage, and duplicate detections.
- Performance may vary with image quality, lighting, viewing angle, and damage type.
- The current evaluation does not establish real-world automotive inspection reliability.
- Visual improvements to the interface do not improve model accuracy.
- A human inspector must verify the predictions.

**Do not use this prototype as the sole basis for vehicle safety, roadworthiness, repair, insurance, or pass/fail decisions.**

## 13. Future Improvements

- Improve dataset quality and annotation consistency.
- Increase and diversify training examples for each damage class.
- Evaluate per-class precision, recall, and mAP.
- Reduce false-positive and duplicate detections.
- Test on a representative, separate collection of vehicle images.
- Improve confidence calibration and detection localization.
- Add structured human-review workflows.
- Validate the system thoroughly before considering any practical deployment.

## 14. Deployment Status

The application is designed to run locally using Streamlit. Deployment to Streamlit Community Cloud can be completed after the project has been pushed to GitHub.

**Streamlit app:** Add the published URL here after deployment succeeds.

## 15. Author and Links

**Rohit Rajaram Yadav**  
B.Tech — Automation & Robotics Engineering

- **GitHub:** https://github.com/ar-rohit01
- **LinkedIn:** https://www.linkedin.com/in/rohit-yadav-6b8999299/

---

*This project is an educational computer-vision prototype. Its predictions require human verification and are not a substitute for professional vehicle inspection.*
