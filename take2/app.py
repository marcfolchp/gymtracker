import streamlit as st
import streamlit_authenticator as stauth
import subprocess

import yaml
from yaml.loader import SafeLoader

with open('credentials.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login('Login', 'main')

st.session_state

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
    st.write(st.session_state)

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

# Display signup button
if st.button('Sign Up'):
    # Use subprocess to execute the other Python script
    subprocess.run(['bash','registration.py'])