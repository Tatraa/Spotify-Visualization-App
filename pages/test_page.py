import pandas as pd
import streamlit as st
import numpy as np

@st.cache_data
def load_data(path:str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"\n[FAILED] path '{path}' doesn't exist!")


def home_page(data):
    options_for_sidebar = st.sidebar.button("option1")
    st.title("TESTING PAGE FROM pages/test_page.py")
    st.dataframe(data)

def main():
    data = load_data("csvs/spotify_2010_2019_data.csv")
    home_page(data)

main()