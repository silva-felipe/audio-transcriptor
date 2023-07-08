import os
from dotenv import load_dotenv
import openai
from pydub import AudioSegment
import streamlit as st

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def split_audio(filename, chunk_length_ms=120000):  # default chunk length is 60 seconds
    audio = AudioSegment.from_file(filename)
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunks.append(audio[i:i+chunk_length_ms])
    return chunks

@st.cache_data
def transcript(filename):
    base_filename = os.path.basename(filename).replace('.mp4', '')
    chunks = split_audio(filename)
    transcripts = []
    for i, chunk in enumerate(chunks):
        chunk_filename = f"./transcripts/{base_filename}_chunk{i}.wav"
        chunk.export(chunk_filename, format="wav")  # save chunk to a temporary file
        with open(chunk_filename, "rb") as audio_file:
            response = openai.Audio.transcribe("whisper-1", audio_file)
            transcripts.append(response['text'])
        os.remove(chunk_filename)  # delete the temporary file

    # join all transcripts into a single string
    transcripts = " ".join(transcripts)

    with open(f"./transcripts/{base_filename}.txt", "w") as f:
        f.write(transcripts)
    
    return transcripts

# print(transcript("./downloads/IA CÂMERA 3D e INFRAVERMELHO conheça o FREE FLOW.mp4"))