import streamlit as st
import pandas as pd
from pymongo import MongoClient
from datetime import datetime

connection_string = "mongodb+srv://marcfolchpomares:AstonMartin1@mycluster.e19nlo1.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db = client.ELO_gym
collection = db.data
cursor = collection.find({})
data = list(cursor)
df = pd.DataFrame(data)

bodypart = df["Bodypart"].unique()

st.markdown("""
	<style>
	@import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap");

	.stSelectbox:first-of-type > div[data-baseweb="select"] > div {
	      padding: 10px;
	      font-family: 'Space Grotesk', sans-serif;
	}
	</style>
""", unsafe_allow_html=True)

selected_bodypart = st.selectbox('Bodypart:', bodypart)

data = df[["Date", "Bodypart", "Exercise", "Weight", "Repetitions", "Score"]]
grouped = data.groupby(["Bodypart", pd.to_datetime(data['Date']).dt.date]).agg({'Score': 'mean'}).astype(int).reset_index()
latest_index = grouped.groupby('Bodypart')['Date'].idxmax()
latest_scores = grouped.loc[latest_index]
latest_score = latest_scores[latest_scores["Bodypart"]==selected_bodypart]["Score"]

style_html = f'<style>'
style_html += f'@import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap");'
style_html += f'.price_details {{'
style_html += f'    font-size: 80px; '
style_html += f'    font-family: "Space Grotesk", sans-serif;'
style_html += f'    color: #f6f6f6;'
style_html += f'    font-weight: 900;'
style_html += f'    text-align: center;'
style_html += f'    line-height: 1;'
style_html += f'    margin-bottom: 100px;'
style_html += f'}}'
style_html += f'.btc_text {{'
style_html += f'    font-size: 20px;'
style_html += f'    font-family: "Space Grotesk", sans-serif;'
style_html += f'    color: #a1a1a1;'
style_html += f'    font-weight: bold;'
style_html += f'    text-align: center;'
style_html += f'    line-height: 0.2;'
style_html += f'    padding-top: 10px;'
style_html += f'}}'
style_html += f'</style>'

# Replace the placeholder {elo} with the value of back_scores.item()
html_content = f'<p class="btc_text">ELO<br></p>'
html_content += f'<p class="price_details">{latest_score.item()}</p>'

# Combine style and HTML content
full_html = style_html + html_content

# Display the HTML using st.markdown
st.markdown(full_html, unsafe_allow_html=True)