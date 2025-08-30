# 🧠 YouTube Abstractive Summarizer (LaMini-Flan-T5)

This project is a web application that takes a YouTube video URL and returns an **AI-generated summary** along with a downloadable **MP3 audio version** of the summary.

Built using:
- 🤖 [MBZUAI/LaMini-Flan-T5-248M](https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M) for abstractive summarization
- 📜 `youtube-transcript-api` for fetching subtitles
- 🎧 `gTTS` for converting the summary into speech
- 🌐 `Streamlit` for a clean and interactive web UI

---

## 🚀 Features

- 📺 Accepts YouTube links
- ✍️ Extracts English transcript
- 🧠 Summarizes using a T5-based model
- 🎵 Converts the summary to an MP3 file
- 📥 Option to download the audio
- 💻 Simple UI with Streamlit

---

## 📁 Project Structure

```
.
├── summarizer.py              # Core logic: fetch transcript, summarize, save audio
├── app_summarizer.py          # Streamlit UI
├── YouTube Summarizer.ipynb   # Jupyter notebook version (for experimentation)
└── requirements.txt           # Python dependencies
```


---

## 📺 Live Demo

Check out the deployed Streamlit app here:  
👉 [YouTube Abstractive Summarizer](https://youtube-abstractive-summarizer-5e46mfhrcuhfwekdyyehxv.streamlit.app/)


