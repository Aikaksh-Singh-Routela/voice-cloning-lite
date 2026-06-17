import streamlit as st
from gtts import gTTS
import io

st.set_page_config(
    page_title="Voice Cloning App (Lite)",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 Voice Cloning App (Lite)")
st.markdown("*Generate speech from text using AI (gTTS)*")

with st.sidebar:
    st.header("⚙️ Settings")
    language = st.selectbox("Language", ["en", "es", "fr", "de", "hi", "zh-cn"])
    slow = st.checkbox("Slow Speed", value=False)

text_to_speak = st.text_area(
    "Enter text to speak",
    "Hello, this is a voice generated using AI!",
    height=150
)

if st.button("🔊 Generate Speech"):
    if text_to_speak:
        try:
            tts = gTTS(text=text_to_speak, lang=language, slow=slow)
            audio_bytes = io.BytesIO()
            tts.write_to_fp(audio_bytes)
            audio_bytes.seek(0)
            st.audio(audio_bytes, format='audio/mp3')
            st.download_button(
                "⬇️ Download Audio (MP3)",
                audio_bytes,
                file_name="generated_speech.mp3",
                mime="audio/mp3"
            )
            st.success("✅ Speech generated successfully!")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter some text.")

st.markdown("---")
st.caption("🎤 Voice Cloning Lite - Powered by gTTS")