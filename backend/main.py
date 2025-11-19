from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from utils.transcriber import transcribe_audio
from utils.summarizer import summarize_text
from utils.highlight_extractor import extract_highlights
from utils.audio_cleaner import enhance_audio
from utils.visual_generator import generate_story_visual
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/process-audio")
async def process_audio(file: UploadFile):

    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    enhanced_path = enhance_audio(temp_path)
    transcript = transcribe_audio(enhanced_path)
    summary = summarize_text(transcript)
    highlights = extract_highlights(transcript)
    visual_path = generate_story_visual(summary)

    os.remove(temp_path)

    return {
        "transcript": transcript,
        "summary": summary,
        "highlights": highlights,
        "visual_image_path": visual_path,
    }
