import pandas as pd
import streamlit as st
import numpy as np
import charts

st.set_page_config(layout='wide')

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

    # testowanie spotipy na test page'u
    container = st.container()
    selected_artist = st.selectbox('Wybierz artyste', data['artist'])
    #selected_albums = st.selectbox('Wybierz artyste', data['albums'])
    with container:
        st.title("Spotify")
        charts.spotifyProfilePicture(selected_artist)


def main():
    data = load_data("csvs/spotify_2010_2019_data.csv")
    home_page(data)

main()