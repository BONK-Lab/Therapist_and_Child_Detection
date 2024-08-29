# Therapist_and_Child_Detection
# YOLO Object Tracking with Video Selection and Webcam Support

This project demonstrates how to use a pre-trained YOLO model for object tracking, allowing users to select a video file or use their webcam as the video source. The YOLO model is trained with GVision data.

## Features

- **Select Video File:** Use a file dialog to select a video file for object tracking.
- **Webcam Support:** Track objects using your webcam as the video source.
- **Real-Time Tracking:** The results are displayed in real-time with the ability to see the tracked objects.

## Requirements

Make sure you have the following installed:

- Python 3.x
- OpenCV (`opencv-python`)
- Tkinter (usually included with Python installations)
- Ultralytics YOLO (`ultralytics`)

## Installation

1. Clone the repository or download the script.
2. create a conda envirnment
3. activate the envirnment 
4. Install the required packages using pip:

   ```bash
   pip install ultralytics opencv-python
   ```

## Yolov8

I have used gvision library to train the data set from roboflow [gvision](https://github.com/gaurang157/gvision)


## Run

Run the following command after getting your conda environment setup.

```bash
python app.py
```
