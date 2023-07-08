import streamlit as st
import os
from helper.downloader import Downloader
from helper.transcript import transcript

with st.container():
    st.write("Let's Transcript!")

with st.container():
    url = st.text_input("Enter the YouTube video URL: ", key="url")
    st.caption("Allowed file formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm.")

    if url == "":
        st.warning("Please enter a YouTube video URL")
    else:
        print(url)

        video_title = Downloader(url).download_video()

        transcript = transcript(f"{video_title}.mp4")

        st.write(transcript)
