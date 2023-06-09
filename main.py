import streamlit as st
from pytube import YouTube

url = st.text_input("Enter Video Link...")
st.title = "Video Downloader by Erhan"

if len(url) > 0:
    yt = YouTube(url)
    result = yt.streams.get_highest_resolution().download()

    with open(result, 'rb') as file:
        btn = st.download_button(
            label="Download Video",
            data=file,
            file_name=str(yt.title + ".mp4"),
            mime="video/mp4"
        )
