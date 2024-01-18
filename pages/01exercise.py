import streamlit as st
from new import graph
import pandas as pd
import matplotlib.pyplot as plt
import warnings

def main():
    st.title("Progress")

    exercises = pd.read_csv("table.csv")
    exercise_options = exercises["Exercise"].unique().tolist()
    exercise = st.selectbox("Exercise:", exercise_options)

    lastrow = pd.read_csv("table.csv")

    lastrow = lastrow[lastrow["Exercise"]==exercise]

    graph = pd.read_csv("table.csv")
    graphs = graph[graph["Exercise"]==exercise][["Date", "Score"]].groupby("Date").mean()

    # Button to trigger the function
    if st.button("Enter"):

        # st.write(lastrow.iloc[-1])

        # Create a separate figure and axes
        fig, ax = plt.subplots()

        # Use the axes to plot
        ax.plot(graphs.index, graphs["Score"])

        # Display the plot using st.pyplot
        st.pyplot(fig)

if __name__ == "__main__":
    main()