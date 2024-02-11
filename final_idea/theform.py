import streamlit as st
import pandas as pd
from pymongo import MongoClient
from datetime import datetime, timedelta
import pytz

connection_string = "mongodb+srv://marcfolchpomares:AstonMartin1@mycluster.e19nlo1.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db = client.ELO_gym
collection = db.data

def calculator (weight, repetitions):
    return ((weight/5)*12)+(repetitions-(2*(weight/5)))

cursor = collection.find({})
data = list(cursor)
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

bodypart = df["Bodypart"].unique()
selected_bodypart = st.selectbox('Bodypart:', bodypart)

exercise = list(df[df["Bodypart"] == selected_bodypart]["Exercise"].unique()) + ["New"]

selected_exercise = st.selectbox('Exercise:', exercise)

if selected_exercise == 'New':
    selected_exercise = st.text_input('Enter a new exercise:')

selected_weight = st.number_input("Weight:", step=0.1)

selected_repetitions = st.number_input("Repetitions:", step=1)

collection = db.data

now_utc = datetime.now() - timedelta(hours=5)

new_row_data = {"Date":now_utc, "Bodypart":selected_bodypart, "Exercise":selected_exercise, "Weight":selected_weight, "Repetitions":selected_repetitions, "Score":calculator(selected_weight, selected_repetitions)}

if st.button("Insert"):
    collection.insert_one(new_row_data)

today_date = pd.to_datetime('today').normalize()
df2 = df[df['Date'] < today_date]

# Assuming 'selected_exercise' is the exercise you want to filter by
last_exercise = df2[df2["Exercise"] == selected_exercise]

# Get the maximum date
max_date = pd.to_datetime(last_exercise['Date']).dt.date.max()

# Select all rows where the 'Date' column is less than the maximum date
latest_rows = last_exercise[last_exercise['Date'].dt.date == max_date]

latest_rows[["Weight", "Repetitions"]]