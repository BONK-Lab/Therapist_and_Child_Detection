import cv2
from ultralytics import YOLO
from tkinter import Tk, filedialog
import os

def select_video():
    root = Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(
        title="Select a Video File",
        filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")]
    )
    return file_path


model = YOLO('best.pt')

print("Select an option:")
print("1. Select a video file")
print("2. Use webcam")
option = input("Enter option (1/2): ")

if option == '1':
    video_path = select_video()
    if not video_path:
        print("No video selected. Exiting...")
    else:
        # Track objects in the selected video
        results = model.track(source=video_path, show=True, tracker='bytetrack.yaml')
elif option == '2':
    print("Using webcam...")
    # Track objects using webcam (source=0)
    results = model.track(source=0, show=True, tracker='bytetrack.yaml')
else:
    print("Invalid option. Exiting...")
