# Use an official Python runtime as a parent image
FROM python:3.11-bullseye

# Set the working directory to /app
WORKDIR /app

# Install Node.js, Git, FFmpeg, and nano
RUN apt-get update && \
    apt-get install -y curl git build-essential ffmpeg nano && \
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the modified authenticate.py file
COPY ./helper/cipher.py /usr/local/lib/python3.11/site-packages/pytube/cipher.py

# create transcripts and download directory
RUN mkdir ./transcripts

RUN mkdir ./downloads

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run app.py when the container launches
CMD ["streamlit", "run", "streamlit_transcriptor.py"]
