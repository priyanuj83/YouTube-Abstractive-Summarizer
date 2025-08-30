import re
from pytube import extract
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from gtts import gTTS
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch


MODEL_NAME = "MBZUAI/LaMini-Flan-T5-248M"
device = 0 if torch.cuda.is_available() else -1

# Load summarizer once
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if device == 0 else torch.float32
)
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, device=device)


def extract_video_id(url: str) -> str:
    return extract.video_id(url)

def fetch_transcript(video_id: str) -> str:
    """
    Fetch English transcript using YouTubeTranscriptApi v2.x.
    """
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id, languages=["en", "en-US", "en-GB"])
        return " ".join(snippet.text for snippet in transcript if snippet.text.strip())
    except (TranscriptsDisabled, NoTranscriptFound):
        raise RuntimeError("Captions are disabled or unavailable for this video.")


def summarize_text(text: str, chunk_size=450) -> str:
    """Summarize long text by chunking."""
    words = text.split()
    if len(words) <= 120:
        return summarizer(f"summarize: {text}", max_length=180, min_length=60, truncation=True)[0]["summary_text"]
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    partials = [summarizer(f"summarize: {c}", max_length=180, min_length=60, truncation=True)[0]["summary_text"] for c in chunks]
    return summarizer(" ".join(partials), max_length=220, min_length=80, truncation=True)[0]["summary_text"]


def save_audio(text: str, path: str = "summary.mp3") -> str:
    gTTS(text=text, lang="en").save(path)
    return path
