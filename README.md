# AUDIO-TRANSCRIPT STREANLIT APP
## App Description
This app is intended to transcript the audio of a video either from an youtube video url with the possibility to download it and the transcription will be saved as a .txt file or from a local video file and the transcription will be displayed in the app and also downloaded.


## create a python environment
```python3 -m venv .```

```source env/bin/activate```

```pip install -r requirements.txt```

## activate environment
```source env/bin/activate```

## substitute the script cipher.py from helper directory to the lib pytube
```cp -r helper/cipher.py lib/pytube```

### ***or substitute the following lines***

new line 272: `r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',`

new line 273: `r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',`


## run the app
```streamlit run streamlit_transcriptor.py```

## stop the app
```CTRL + C```

## deactivate environment
```deactivate```

# Run the app using Docker

## build the image
```docker build -t streamlit-transcriptor .```

## run the image
```docker run -p 8501:8501 streamlit-transcriptor```

## stop the image
```docker stop <container_id>```

## remove the image
```docker rmi streamlit-transcriptor```

## run the image in detached mode
```docker run -d -p 8501:8501 streamlit-transcriptor```

# Deploy on GCP
- Connect to the Google Cloud SDK: Ensure that you have installed and configured the Google Cloud SDK on your computer. If you haven't already done so, follow the instructions provided by Google to install the SDK for your operating system. Once installed, connect to your Vitalwork project using the command:

    - run: ```gcloud auth login``` 

- Navigate to the directory: Navigate to the directory where the dashboard streamlit project is located. Ensure that you are in the root directory of the project.
    - run: ```gcloud builds submit . --tag gcr.io/audio-transcriptor-392502/audio-transcriptor```

    - run: ```gcloud run deploy --image gcr.io/audio-transcriptor-392502/audio-transcriptor --platform managed --port 8501 --region us-central1 --allow-unauthenticated```