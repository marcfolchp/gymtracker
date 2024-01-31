# IMPORT LIBRARIES

import streamlit as st
import pandas as pd
from pymongo import MongoClient



# OPEN OBJECTIVES TABLE

connection_string = "mongodb+srv://marcfolchpomares:AstonMartin1@mycluster.e19nlo1.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db = client.ELO_gym
collection = db.objectives

cursor = collection.find({})
data = list(cursor)
df = pd.DataFrame(data)



# FORM AND TRANSFORMATION

bodypart = df["Bodypart"].unique()
selected_bodypart = st.selectbox('Bodypart:', bodypart)

exercise = df[df["Bodypart"] == selected_bodypart]["Exercise"].unique()
selected_exercise = st.selectbox('Exercise:', exercise)

selected_weight = st.number_input("Weight:", step=0.1)

selected_repetitions = st.number_input("Repetitions:", step=1)

converter = 0.453592
multiplier = 1.899371069

def calculator (weight, repetitions):
    return ((weight/5)*16)+(repetitions-(3*(weight/5)))

elo = ((calculator(selected_weight*converter, selected_repetitions) - df[df["Exercise"]==selected_exercise]["Actual Score"].item()) / (df[df["Exercise"]==selected_exercise]["Goal Score"].item() - df[df["Exercise"]==selected_exercise]["Actual Score"].item()) * 2400)



# OPEN DATA TABLE TO CREATE A NEW ROW WHEN FORM SUBMITTED

from datetime import datetime
collection = db.data

current_datetime = datetime.now()
new_row_data = {"Date":current_datetime, "Bodypart":selected_bodypart, "Exercise":selected_exercise, "Weight":selected_weight, "Repetitions":selected_repetitions, "ELO":elo}

if st.button("Insert"):
    collection.insert_one(new_row_data)