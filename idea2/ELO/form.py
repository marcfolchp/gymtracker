import streamlit as st
st.write("Hello")

import pandas as pd
from pymongo import MongoClient

# Replace these values with your MongoDB Atlas connection string and database/collection information
connection_string = "mongodb+srv://marcfolchpomares:AstonMartin1@mycluster.e19nlo1.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB Atlas
client = MongoClient(connection_string)

# Access a specific database (replace 'your_database' with your actual database name)
db = client.ELO_gym

# Access a specific collection within the database (replace 'your_collection' with your actual collection name)
collection = db.objectives

# Query all documents from the collection
cursor = collection.find({})
data = list(cursor)

# Create a DataFrame from the retrieved data
df = pd.DataFrame(data)

bodypart = df["Bodypart"].unique()

# Create a select box
selected_bodypart = st.selectbox('Bodypart:', bodypart)

exercise = df[df["Bodypart"] == selected_bodypart]["Exercise"].unique()

# Create a select box
selected_exercise = st.selectbox('Exercise:', exercise)

selected_weight = st.number_input("Weight:", step=0.1)

selected_repetitions = st.number_input("Repetitions:", step=1)


# Access a specific collection within the database (replace 'your_collection' with your actual collection name)
collection = db.data

from datetime import datetime

# Get current date and time
current_datetime = datetime.now()

new_row_data = {"Date":current_datetime, "Bodypart":selected_bodypart, "Exercise":selected_exercise, "Weight":selected_weight, "Repetitions":selected_repetitions}

if st.button("Insert"):
    collection.insert_one(new_row_data)