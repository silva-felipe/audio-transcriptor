import streamlit as st
import os
from helper.downloader import Downloader
from helper.transcript import transcript

with st.container():
    st.write("Let's Transcript!")

with st.container():
    url = st.text_input("Enter the YouTube video URL: ", key="url", help="Allowed file formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm.")
    # st.caption("Allowed file formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm.")

    if url == "":
        st.warning("Please enter a YouTube video URL")
    else:
        video_title = Downloader(url).download_video()

        transcript_text = transcript(f"downloads/{video_title}.mp4")

        st.write(transcript_text)

        # Add download buttons for the video and the transcript
        st.download_button(
            label="Download Video",
            data=open(f"downloads/{video_title}.mp4", "rb"),
            file_name=f"{video_title}.mp4",
            mime="video/mp4",
        )
        st.download_button(
            label="Download Transcript",
            data=open(f"transcripts/{video_title}.txt", "r"),
            file_name=f"{video_title}.txt",
            mime="text/plain",
        )