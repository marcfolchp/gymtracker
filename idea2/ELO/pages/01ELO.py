import streamlit as st
import pandas as pd
from pymongo import MongoClient
import pathlib 
import shutil

import streamlit.components.v1 as components

# HACK This works when we've installed streamlit with pip/pipenv, so the
# permissions during install are the same as the running process
STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
# We create a videos directory within the streamlit static asset directory
# and we write output files to it
VIDEOS_PATH = (STREAMLIT_STATIC_PATH / "styles")
if not VIDEOS_PATH.is_dir():
    VIDEOS_PATH.mkdir()

wildlife_video = VIDEOS_PATH / "style.css"
if not wildlife_video.exists():
    shutil.copy("style.css", wildlife_video)  # For newer Python.

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

connection_string = "mongodb+srv://marcfolchpomares:AstonMartin1@mycluster.e19nlo1.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db = client.ELO_gym
collection = db.data

cursor = collection.find({})
data = list(cursor)

# Create a DataFrame from the retrieved data
data = pd.DataFrame(data)

bodypart = data["Bodypart"].unique()

selected_bodypart = st.selectbox("Bodypart:",bodypart)

elo = round(data[data["Bodypart"]==selected_bodypart]["ELO"].mean(), 0)

st.markdown(f'<p class="btc_text">ELO<br></p><p class="price_details">{elo}</p>', unsafe_allow_html = True)