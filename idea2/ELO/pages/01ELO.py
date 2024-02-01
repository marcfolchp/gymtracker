import streamlit as st
import pandas as pd
from pymongo import MongoClient

with open('../style.css') as f:
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