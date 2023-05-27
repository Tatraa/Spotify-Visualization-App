import streamlit as st
import plotly_express as px
import plotly as pt
import pandas as pd
import logging
import numpy as np


@st.cache_data
def load_data(path:str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"\n[FAILED] path '{path}' doesn't exist!")


def home_page(data):
    # Using object notation
    st.title("Home Page")
    chart_data = data[["bpm", "nrgy"]]


    with st.container():
        fig = px.scatter(
            chart_data,
            x="bpm",
            y="nrgy",
            size='bpm',
            color="bpm",
            hover_name="bpm",
            log_x=True,
            size_max=160,
        )
        st.plotly_chart(fig,theme=None,height=800,width=1500)

    with st.container():
        st.header("Bar Chart")
        st.bar_chart(chart_data)

def main():
    data = load_data("csvs/spotify_2010_2019_data.csv")
    home_page(data)

main()











