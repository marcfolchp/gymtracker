import streamlit as st
import pandas as pd
from pymongo import MongoClient
from datetime import datetime

connection_string = "mongodb+srv://marcfolchpomares:AstonMartin1@mycluster.e19nlo1.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db = client.ELO_gym
collection = db.data

def calculator (weight, repetitions):
    return ((weight/5)*12)+(repetitions-(2*(weight/5)))

cursor = collection.find({})
data = list(cursor)
df = pd.DataFrame(data)

bodypart = df["Bodypart"].unique()
selected_bodypart = st.selectbox('Bodypart:', bodypart)

exercise = list(df[df["Bodypart"] == selected_bodypart]["Exercise"].unique()) + ["New"]

selected_exercise = st.selectbox('Exercise:', exercise)

if selected_exercise == 'New':
    selected_exercise = st.text_input('Enter a new exercise:')

selected_weight = st.number_input("Weight:", step=0.1)

selected_repetitions = st.number_input("Repetitions:", step=1)

collection = db.data

current_datetime = datetime.now()
new_row_data = {"Date":current_datetime, "Bodypart":selected_bodypart, "Exercise":selected_exercise, "Weight":selected_weight, "Repetitions":selected_repetitions, "Score":calculator(selected_weight, selected_repetitions)}

if st.button("Insert"):
    collection.insert_one(new_row_data)

last_exercise = df[(df["Exercise"]==selected_exercise)]

max_date = pd.to_datetime(last_exercise['Date']).dt.date.max()

# Select all rows where the 'Date' column matches the maximum date
latest_rows = last_exercise[last_exercise['Date'].dt.date == max_date]

# Print or use the rows with the latest date as needed
latest_rows[["Weight", "Repetitions"]]