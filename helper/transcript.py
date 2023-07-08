import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def transcript(filename):
    audio_file = open(filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    # with open(f"transcript_{filename}", "w") as f:
    #     f.write(transcript['text'])

    return transcript['text']

transcript("/Volumes/My Passport/personal/audio-transcript/Why Failure is Actually Success in Disguise.mp4")