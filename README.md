# 🚦 Smart Traffic Management System

This project is a **Smart Traffic Management System** that uses **YOLOv8 (You Only Look Once)** for real-time vehicle detection.  
The system analyzes traffic images, counts vehicles, and dynamically calculates green light duration based on traffic density.  

---

## 📌 Features
- Upload traffic images via a simple **Flask web app**.
- Detect vehicles (car, bike, bus, truck) using **YOLOv8**.
- Display annotated images with bounding boxes.
- Dynamically calculate **green light duration**:
  - ≤ 5 vehicles → 10 seconds  
  - ≤ 10 vehicles → 15 seconds  
  - > 10 vehicles → `2 × vehicle_count` seconds

---

## 🛠️ Tech Stack
- **Python**
- **Flask** – Web framework
- **YOLOv8 (Ultralytics)** – Object detection
- **OpenCV** – Image processing
- **HTML + CSS** – Frontend

---

## 📂 Project Structure
smart-traffic-system/
│── app.py # Flask web application
│── templates/
│ ├── index.html # Upload page
│ ├── result.html # Results display page
│── static/
│ └── processed/ # Annotated images
│── uploads/ # Uploaded images
│── requirements.txt # Dependencies
│── README.md # Project documentation
