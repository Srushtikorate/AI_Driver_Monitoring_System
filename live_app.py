import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av
import cv2
import pandas as pd
import joblib
from math import hypot
from cvzone.FaceMeshModule import FaceMeshDetector

# Load ML Model
model = joblib.load("driver_model.pkl")

st.set_page_config(
    page_title="AI Driver Monitoring System",
    layout="wide"
)

st.title("AI Driver Monitoring System")

# Reduce page width
st.markdown("""
<style>
.block-container {
    max-width: 1100px;
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)


class FaceMeshProcessor(VideoProcessorBase):

    def __init__(self):
        self.detector = FaceMeshDetector(maxFaces=1)

    def recv(self, frame):

        img = frame.to_ndarray(format="bgr24")

        img, faces = self.detector.findFaceMesh(img, draw=True)

        if faces:

            face = faces[0]

            # --------------------
            # Eye Opening
            # --------------------
            leftUp = face[159]
            leftDown = face[23]

            length = hypot(
                leftDown[0] - leftUp[0],
                leftDown[1] - leftUp[1]
            )

            cv2.putText(
                img,
                f"Eye Opening: {int(length)}",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 0),
                2
            )

            # --------------------
            # Head Direction
            # --------------------
            nose = face[1]
            left_face = face[234]
            right_face = face[454]

            left_dist = abs(nose[0] - left_face[0])
            right_dist = abs(right_face[0] - nose[0])

            direction = "Forward"
            direction_code = 0

            if left_dist - right_dist > 25:
                direction = "Looking Right"
                direction_code = 2

            elif right_dist - left_dist > 25:
                direction = "Looking Left"
                direction_code = 1

            cv2.putText(
                img,
                f"Direction: {direction}",
                (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 0),
                2
            )

            # --------------------
            # Rule Status
            # --------------------
            rule_status = "Alert"

            if length < 8:
                rule_status = "Drowsy"

            if direction != "Forward":
                rule_status = "Distracted"

            cv2.putText(
                img,
                f"Rule Status: {rule_status}",
                (20, 105),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 0),
                2
            )

            # --------------------
            # ML Prediction
            # --------------------
            features = pd.DataFrame(
                [[
                    length,
                    0,
                    0,
                    direction_code
                ]],
                columns=[
                    "Eye_Opening",
                    "Blink_Count",
                    "Closed_Time",
                    "Head_Direction"
                ]
            )

            prediction = model.predict(features)[0]

            status_map = {
                0: "Alert",
                1: "Drowsy",
                2: "Distracted"
            }

            ml_status = status_map[prediction]

            cv2.putText(
                img,
                f"ML Status: {ml_status}",
                (20, 140),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 0),
                2
            )

        return av.VideoFrame.from_ndarray(img, format="bgr24")


# -----------------------------
# Dashboard Layout
# -----------------------------

col1, col2 = st.columns([2, 1])

with col1:

    webrtc_streamer(
        key="driver-monitor",
        video_processor_factory=FaceMeshProcessor,
        media_stream_constraints={
            "video": True,
            "audio": False
        }
    )

with col2:

    st.subheader("System Information")

    st.success("Face Mesh Detection")
    st.success("Eye Opening Detection")
    st.success("Head Direction Detection")
    st.success("Random Forest Classification")
    st.success("Real-Time Monitoring")

    st.markdown("---")

    st.subheader("Project Status")

    st.info("Driver Monitoring Active")
    st.info("Machine Learning Enabled")