from pytube import YouTube

class Downloader:
    def __init__(self, link):
        self.link = link

    def download_video(self):
        youtube_object = YouTube(self.link)
        youtube_object = youtube_object.streams.get_highest_resolution()
        try:
            youtube_object.download(output_path="../downloads/")
            print("Download is completed successfully")
        except:
            
            print("An error has occurred")

        title = youtube_object.title
        title = title.replace("\"", "").replace("?","")

        return title