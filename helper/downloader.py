from pytube import YouTube
import streamlit as st
import re
import os

# Specify the directory you want to ensure exists
directory = './downloads'

# Create the directory if it doesn't exist
os.makedirs(directory, exist_ok=True)

class Downloader:
    def __init__(_self, link):
        _self.link = link

    # @st.cache_data
    def download_video(_self):
        youtube_object = YouTube(_self.link)
        st.image(youtube_object.thumbnail_url)

        youtube_object_streams = youtube_object.streams.get_highest_resolution()
        
        try:
            youtube_object_streams.download(output_path="./downloads/")
            print("Download is completed successfully")
        except Exceprion as e:
            print("An error has occurred", e)


        title = youtube_object.title
        title = re.sub(r'[\\/*?:!"<>|,]', "", title)  # remove any characters that are not valid in filenames

        return title