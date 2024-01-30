import streamlit as st
from new import table
import pandas as pd

def main():
    st.title("Enter Data")

    bodypart_options = ["Pecho", "Hombro", "Triceps", "Espalda", "Biceps", "Antebrazo", "Quadriceps", "Gluteos", "Isquios", "Gemelos"]
    bodypart = st.selectbox("Bodypart:", bodypart_options)

    # Input boxes
    exercises = pd.read_csv("table.csv")
    exercises = exercises[exercises["Training"]==bodypart]
    exercise_options = exercises["Exercise"].unique().tolist()
    exercise = st.selectbox("Exercise:", exercise_options + ["New"])

    if exercise == "New":
        exercise = st.text_input(f"New exercise for {bodypart}:")

    weight = st.number_input("Weight (kg):", step=0.1, value=None)
    repetitions = st.number_input("Repetitions:", value=None, step=1)

    # Button to trigger the function
    if st.button("Enter"):
        table(bodypart, exercise, weight, repetitions)
        bodypart = st.empty()

if __name__ == "__main__":
    main()