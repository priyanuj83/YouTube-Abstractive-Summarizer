import streamlit as st
from summarizer import extract_video_id, fetch_transcript, summarize_text, save_audio

st.set_page_config(page_title="YouTube Abstractive Summarizer", page_icon="🧠", layout="centered")
st.title("🧠 YouTube Abstractive Summarizer (LaMini-Flan-T5)")
st.caption("Paste a YouTube link ➜ get a readable summary + an MP3 🎧")

url = st.text_input("🎥 YouTube URL", placeholder="https://www.youtube.com/watch?v=...")
if st.button("Summarize", type="primary") and url:
    try:
        vid = extract_video_id(url)
        st.components.v1.iframe(f"https://www.youtube.com/embed/{vid}", height=315)

        with st.spinner("📜 Fetching transcript..."):
            transcript = fetch_transcript(vid)

        with st.spinner("✍️ Summarizing..."):
            summary = summarize_text(transcript)

        st.subheader("🧠 AI Summary")
        st.write(summary)

        mp3_path = save_audio(summary, "summary.mp3")
        st.audio(mp3_path)

        with open(mp3_path, "rb") as f:
            st.download_button("📥 Download Summary MP3", f, file_name="summary.mp3")

    except Exception as e:
        st.error(f"❌ {str(e)}")
