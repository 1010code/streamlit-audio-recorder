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
    st.header("🎙️ Audio Recorder")
    def in_recorder_factory() -> MediaRecorder:
        return MediaRecorder(
            "input.wav", format="wav"
        )

    webrtc_ctx = webrtc_streamer(
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
    status_indicator = st.empty()
    try:
        st.audio('input.wav', format="audio/wav")
        clear() # remove audio file
    except:
        status_indicator.write('No record media. Click start button to record audio.')
    
    if webrtc_ctx.state.playing:
        # center layout
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(' ')
        with col2:
            st.image('https://jp.easeus.com/images_2019/multimedia/recexperts/feature-2.gif')
            status_indicator.write('Recording...')
        with col3:
            st.write(' ')

if __name__ == "__main__":
    app()