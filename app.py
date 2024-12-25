import cv2
from ultralytics import YOLO
import streamlit as st
from pathlib import Path
import tempfile
import os

# Load the YOLO model
model = YOLO('best.pt')

def process_video(video_path, use_webcam):
    output_dir = "processed_videos"  # Directory to save the processed videos
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    if use_webcam:
        st.info("Using webcam for tracking...")
        # Track objects using webcam (source=0)
        results = model.track(source=0, show=False, save=True, tracker='bytetrack.yaml')
    else:
        if not video_path:
            st.error("No video selected. Please upload a video file.")
            return

        st.info(f"Processing video: {video_path}...")
        # Track objects in the selected video
        results = model.track(source=video_path, show=False, save=True, tracker='bytetrack.yaml')

    # Get the path of the latest processed video
    latest_run_dir = max(Path(output_dir).glob('*'), key=os.path.getctime)
    processed_video_path = next(latest_run_dir.glob('*.mp4'), None)

    if processed_video_path:
        st.success(f"Processed video saved at: {processed_video_path}")
        return str(processed_video_path)
    else:
        st.error("Processed video not found.")
        return None

# Streamlit App UI
st.title("YOLO Object Tracking")
st.write("Choose an option to track objects in a video file or through your webcam.")

# Option selection
option = st.radio("Select an option:", ["Upload a Video File", "Use Webcam"])

if option == "Upload a Video File":
    # File uploader for video files
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])

    if uploaded_file is not None:
        # Save uploaded video to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as temp_video:
            temp_video.write(uploaded_file.read())
            temp_video_path = temp_video.name

        # Process the uploaded video
        processed_video_path = process_video(temp_video_path, use_webcam=False)

        # Show the processed video on the front end
        if processed_video_path:
            st.video(processed_video_path)
else:
    # Webcam option
    if st.button("Start Webcam Tracking"):
        processed_video_path = process_video(None, use_webcam=True)

        # Show the processed video on the front end
        if processed_video_path:
            st.video(processed_video_path)
