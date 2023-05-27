import streamlit as st
import plotly_express as px
import plotly as pt
import pandas as pd
import logging
import numpy as np


def home_page(data):
    st.title("Home Page")
    chart_data = data[["bpm","nrgy"]]
    st.line_chart(chart_data)

def main():
    df = pd.read_csv("csvs/spotify_2010_2019_data.csv")
    home_page(df)

main()











