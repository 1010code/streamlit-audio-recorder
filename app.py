import os
import streamlit as st
from aiortc.contrib.media import MediaRecorder

from streamlit_webrtc import WebRtcMode, webrtc_streamer

# Remove audio file
def clear():
    # If file exists, delete it
    if os.path.isfile("input.wav"):
        os.remove("input.wav")

def app():
    st.write("Click start button to record audio.")
    def in_recorder_factory() -> MediaRecorder:
        return MediaRecorder(
            "input.wav", format="wav"
        )

    webrtc_streamer(
        key="loopback",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={
            "video": False,
            "audio": True,
        },
        sendback_audio=False,
        in_recorder_factory=in_recorder_factory,
    )
    try:
        st.audio('input.wav', format="audio/wav")
        clear() # remove audio file
    except:
        st.write("No record media.")

if __name__ == "__main__":
    app()