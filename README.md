# 🚨 Fall Detection System

A simple computer vision–based **fall detection system** built using OpenCV (cv2). This project detects possible human falls by analyzing motion and bounding box changes in video frames.

The system uses **motion detection and contour analysis** to identify abnormal movements that may indicate a fall.

---

## 🧠 Method Used

This project uses a **classical computer vision approach** based on:

- Background subtraction  
- Frame differencing  
- Contour detection  
- Bounding box analysis  

Workflow:

1. Capture video frames using OpenCV  
2. Convert frames to grayscale  
3. Apply background subtraction / frame difference  
4. Detect moving contours  
5. Draw bounding boxes around detected objects  
6. Analyze bounding box position and size changes  
7. Detect abnormal movement that may indicate a fall  

This method is lightweight and does not require deep learning models.

---

## ✨ Technologies

- Python  
- OpenCV (cv2)  
- NumPy  

---

## 🚀 Features

- Real-time motion detection  
- Human movement tracking  
- Bounding box visualization  
- Fall detection based on movement patterns  
- Supports webcam and video files  
- Lightweight and fast processing  

---

## 🚦 Running the Project

Clone the Repository
```bash
git clone https://github.com/tegar17/fall-detection.git
cd fall-detection
```
Install Dependencies
```bash
pip install -r requirements.txt
```
Run the Program
```bash
python main.py
```

---

## 🎞️ Preview
