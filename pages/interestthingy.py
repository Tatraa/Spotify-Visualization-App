import pandas as pd
import streamlit as st
import charts

st.set_page_config(layout='wide')

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"\n[FAILED] path '{path}' doesn't exist!")

def runner():
    data = load_data("csvs/artists_data.csv")
    st.title("All-time most streamed artists")

    with st.expander(label="All-time most streamed artists", expanded=True):
        charts.most_streamed_artists(data)

    with st.expander(label="How much artists made?", expanded=True):
        charts.most_streamed_money_maker(data)

runner()