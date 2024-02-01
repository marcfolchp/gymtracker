import streamlit as st
import pandas as pd
from pymongo import MongoClient
import pathlib 
import shutil

import streamlit.components.v1 as components

# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

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

st.markdown(f'''
    <style>
        @import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap");

        body {{
            background-color: #131722;
            color: #f6f6f6;
        }}

        .price_details {{
            font-size: 80px;
            font-family: "Space Grotesk", sans-serif;
            color: #f6f6f6;
            font-weight: 900;
            text-align: center;
            line-height: 1;
            margin-bottom: 100px;
        }}

        .btc_text {{
            font-size: 20px;
            font-family: "Space Grotesk", sans-serif;
            color: #a1a1a1;
            font-weight: bold;
            text-align: center;
            line-height: 0.2;
            padding-top: 10px;
        }}
    </style>
    <p class="btc_text">ELO<br></p>
    <p class="price_details">{elo}</p>
''', unsafe_allow_html=True)