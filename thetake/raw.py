import streamlit as st
import streamlit_authenticator as stauth
from functions import authenticator
from functions import registrator
from functions import cloudation
from functions import exercises



# ------------------------------
# SESSION STATE
# ------------------------------

if 'page_data' not in st.session_state:
    st.session_state.page_data = "login"

if 'username' not in st.session_state:
    st.session_state.username = None



# ------------------------------
# LOGIN PAGE
# ------------------------------

if st.session_state.page_data == "login":
    st.title("Login")
    # Display the button only if authentication status is False
    username = st.text_input("Username:")
    password = st.text_input("Password:")

    if st.button("Login"):
        if authenticator(username, password):
            st.session_state.username = username
            st.session_state.page_data = "main"
            st.experimental_rerun()
        else:
            st.error("Username and/or password are incorrect.")

    if st.button("Register"):
        st.session_state.page_data = "registration"
        st.experimental_rerun()



# ------------------------------
# REGISTRATION PAGE
# ------------------------------

elif st.session_state.page_data == "registration":
    st.title("Registration")

    name = st.text_input("Name:")
    surname = st.text_input("Surname:")
    age = st.text_input("Age:")
    username = st.text_input("Username:")
    password = st.text_input("Password:")

    if st.button("Register"):
        if (len(name) > 0) and (len(surname) > 0) and (len(age) > 0) and (len(username) > 0) and (len(password) > 0):
            registrator(name, surname, age, username, password)
            st.session_state.page_data = "login"
            st.experimental_rerun()
        else:
            st.error("Please fill in the missing fields.")



# ------------------------------
# MAIN PAGE
# ------------------------------

elif st.session_state.page_data == "main":
    # If authentication status is True, display new content
    st.title(f"Welcome, {st.session_state.username}.")

    if st.button("Logout"):
        st.session_state.page_data = "login"
        st.session_state.username = None
        st.experimental_rerun()
    
    bodypart_options = ["Pecho", "Hombro", "Triceps", "Espalda", "Biceps", "Antebrazo", "Quadriceps", "Gluteos", "Isquios", "Gemelos"]
    bodypart = st.selectbox("Bodypart:", bodypart_options)

    exercise = st.selectbox("Exercise:", exercises(st.session_state.username) + ["New"])
    weight = st.number_input("Weight:", step=0.1)
    repetitions = st.number_input("Repetitions:", step=1)

    username = st.session_state.username

    score = (weight) + (float(repetitions)*0.3)

    if st.button("Enter"):
        cloudation(username, bodypart, exercise, weight, repetitions, score)
        bodypart = st.empty()

    # Replace the button with an empty container
    st.empty()

