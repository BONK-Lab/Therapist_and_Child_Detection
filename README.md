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

## Detailed Description of the Logic Behind Analyzing Model Predictions

This script utilizes a pre-trained YOLO (You Only Look Once) model for object detection and tracking. The following is a step-by-step breakdown of the logic and procedures used to analyze the model's predictions.

---

#### 1. **Initialization and Video Source Selection**

1. **Import Necessary Libraries:**
   - `cv2`: This is OpenCV, a library used for computer vision tasks. It handles video input/output and image processing.
   - `YOLO` from `ultralytics`: This imports the YOLO model class from the Ultralytics package. YOLO is a state-of-the-art, real-time object detection system.
   - `Tk` and `filedialog` from `tkinter`: These are used to create a graphical file selection dialog for choosing a video file.
   - `os`: Provides a way of interacting with the operating system, though in this script, it is not used directly.

2. **Function `select_video`:**
   - A simple function that opens a file dialog allowing the user to select a video file from their filesystem.
   - The `Tk()` instance initializes the Tkinter window, which is immediately hidden with `root.withdraw()` to prevent an empty GUI window from showing.
   - `filedialog.askopenfilename` prompts the user to select a video file, and the file path is returned.

3. **Initialize the YOLO Model:**
   - The YOLO model is loaded using the `YOLO` class, with `best.pt` as the pre-trained weights file. This file should contain a model that has been fine-tuned on a specific dataset, likely using GVision data in this context.

4. **Prompt User for Input:**
   - The script prompts the user to choose between two options:
     - Option 1: Select a video file for object tracking.
     - Option 2: Use the webcam for real-time object tracking.

---

#### 2. **Handling Video Input**

1. **Option 1: Video File Selection**
   - If the user selects the first option (`option == '1'`), the script calls `select_video()` to open the file dialog and get the video file path.
   - If no video is selected (i.e., `video_path` is empty), the script prints an error message and exits.
   - If a video is selected, the script calls `model.track()` with the video file as the source, `show=True` to display the results, and `tracker='bytetrack.yaml'` to enable tracking with ByteTrack.

2. **Option 2: Webcam Input**
   - If the user selects the second option (`option == '2'`), the script sets the video source to the default webcam (`source=0`).
   - The same `model.track()` function is used to perform object detection and tracking on the webcam feed.

3. **Error Handling for Invalid Input**
   - If the user inputs an option other than '1' or '2', the script prints an error message and exits.

---

#### 3. **Analyzing Model Predictions**

1. **Object Detection and Tracking:**
   - The `model.track()` method processes each frame of the video (or webcam feed) and applies the YOLO model to detect objects.
   - The `tracker='bytetrack.yaml'` argument specifies the use of the ByteTrack tracking algorithm, which is responsible for associating detected objects across frames, thereby maintaining their identities.

2. **Visualizing Predictions:**
   - The `show=True` argument in `model.track()` enables real-time visualization of the tracking results. Detected objects are typically highlighted with bounding boxes, and each object is assigned a unique ID to track its movement across frames.

3. **Output Results:**
   - The script processes the entire video or webcam feed, displaying the tracked objects in a window. The results can include details like the bounding box coordinates, class labels, and confidence scores for each detected object.

4. **Reproducing Results:**
   - To reproduce the results, ensure that the `best.pt` model file is available, and the correct version of the `ultralytics` package is installed.
   - Run the script, select a video file or use the webcam, and observe the model's predictions in real-time.

---

### Conclusion

This script provides a straightforward way to apply a pre-trained YOLO model to a video file or webcam feed for object detection and tracking. By following the described steps, an evaluator can easily reproduce the results and understand the underlying logic behind the model's predictions. The combination of user input handling, video processing, and real-time visualization makes this tool versatile for various object tracking applications.

