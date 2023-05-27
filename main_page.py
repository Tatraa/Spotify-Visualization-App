import streamlit as st
import plotly_express as px
import plotly as pt
import pandas as pd
import logging
import numpy as np

from csv_processor import CSVDataProcessor

def home_page(data_csv:"CSVDataProcessor"):
    st.title("Home Page")

    chart_data = data_csv.data[['bpm','nrgy']]
    st.line_chart(chart_data)


def main():
    data = CSVDataProcessor("csvs/spotify_2010_2019_data.csv")
    data.load_csv()
    home_page(data)

main()











