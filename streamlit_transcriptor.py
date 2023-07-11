import streamlit as st
import os
from helper.downloader import Downloader
from helper.transcript import transcript


st.set_page_config(
    page_title="Transcriptor",
    page_icon="🎬",)

def main():
    st.write("Let's Transcript!")

    st.markdown("""
            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9198538794573402"
                crossorigin="anonymous"></script>
            <!-- display add square -->
            <ins class="adsbygoogle"
                style="display:block"
                data-ad-client="ca-pub-9198538794573402"
                data-ad-slot="6206833314"
                data-ad-format="auto"
                data-full-width-responsive="true"></ins>
            <script>
                (adsbygoogle = window.adsbygoogle || []).push({});
            </script>
                """, unsafe_allow_html=True)

    transcript_text = ""  # Initialize transcript_text as an empty string
    file_name = ""  # Initialize file_name as an empty string
    file_extension = ""  # Initialize file_extension as an empty string

    url = st.text_input("Enter the YouTube video URL: ", key="url")
    uploaded_file = st.file_uploader("Or choose a file", type=["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"],
                                    help="Allowed file formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm.")

    if url == "" and uploaded_file is None:
        st.warning("Please enter a YouTube video URL or upload a file")
    elif url != "":
        video_title = Downloader(url).download_video()
        transcript_text = transcript(f"downloads/{video_title}.mp4")
        file_name = video_title
        file_extension = ".mp4"
    elif uploaded_file is not None:  # uploaded_file is not None
        # Save the uploaded file to the downloads directory
        with open(f"downloads/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        transcript_text = transcript(f"downloads/{uploaded_file.name}")
        file_name, file_extension = os.path.splitext(uploaded_file.name)

    st.write(transcript_text)

    # Add download buttons for the video and the transcript
    if file_name != "":
        with open(f"downloads/{file_name}{file_extension}", "rb") as f:
            st.download_button(
                label="Download File",
                data=f.read(),
                file_name=f"{file_name}{file_extension}",
                mime="application/octet-stream",
            )
        if os.path.exists(f"transcripts/{file_name}.txt"):
            with open(f"transcripts/{file_name}.txt", "r") as f:
                st.download_button(
                    label="Download Transcript",
                    data=f.read(),
                    file_name=f"{file_name}.txt",
                    mime="text/plain",
                )

if __name__ == "__main__":
    main()
