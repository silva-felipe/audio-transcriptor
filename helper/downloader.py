from pytube import YouTube
import streamlit as st
import re

class Downloader:
    def __init__(_self, link):
        _self.link = link

    @st.cache_data
    def download_video(_self):
        youtube_object = YouTube(_self.link)
        youtube_object = youtube_object.streams.get_highest_resolution()
        try:
            youtube_object.download(output_path="./downloads/")
            print("Download is completed successfully")
        except Exceprion as e:
            print("An error has occurred", e)

        title = youtube_object.title
        title = re.sub(r'[\\/*?:"<>|,]', "", title)  # remove any characters that are not valid in filenames

        return title