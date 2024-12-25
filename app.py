import cv2
from ultralytics import YOLO
import streamlit as st
from pathlib import Path
import tempfile

# Load the YOLO model
model = YOLO('best.pt')

def process_video(video_path, use_webcam):
    output_dir = "processed_videos"  # Directory to save the processed videos
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    if use_webcam:
        st.info("Using webcam for tracking...")
        # Track objects using webcam (source=0)
        results = model.track(source=0, show=True, save=True, tracker='bytetrack.yaml')
    else:
        if not video_path:
            st.error("No video selected. Please upload a video file.")
            return

        st.info(f"Processing video: {video_path}...")
        # Track objects in the selected video
        results = model.track(source=video_path, show=True, save=True, tracker='bytetrack.yaml')

    # Inform the user where the video is saved
    st.success(f"Processed video saved in: {Path(output_dir).absolute()}")

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
        process_video(temp_video_path, use_webcam=False)
else:
    # Webcam option
    if st.button("Start Webcam Tracking"):
        process_video(None, use_webcam=True)
