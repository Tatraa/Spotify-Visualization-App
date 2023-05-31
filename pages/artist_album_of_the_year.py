import streamlit as st
import spotipy

import charts
from spotifySt import *

st.set_page_config(layout='wide')
# TODO:
# Filtrowanie po artystach i albumach roku, dołączenie analizy danych - 31.05.2023

class Album:
    def __init__(self, ars_name, rel_date, gens, descs, avg_rat, duration_ms, album):
        self.ars_name = ars_name
        self.rel_date = rel_date
        self.gens = gens
        self.descs = descs
        self.avg_rat = avg_rat
        self.duration_ms = duration_ms
        self.album = album
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

@st.cache
def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"\n[FAILED] path '{path}' doesn't exist!")

def run():
    data = load_data("csvs/Top5000_album_rating.csv")
    st.title("Top Albums")

    container = st.container()
    container_for_each_result = st.container()

    num_albums = st.number_input("Enter the number of albums to display:", min_value=1, max_value=len(data), value=10, step=1)
    top_albums = []

    for index, row in data.iterrows():
        album = Album(row['ars_name'], row['rel_date'], row['gens'], row['descs'], row['avg_rat'], row['duration_ms'], row['album'])
        album.add_album(album)
        if len(top_albums) < num_albums:
            top_albums.append(album)
        else:
            min_rating = min(top_albums, key=lambda x: x.avg_rat)
            if album.avg_rat > min_rating.avg_rat:
                top_albums.remove(min_rating)
                top_albums.append(album)

    for album in top_albums:
        with container_for_each_result:
            st.write(f"Artist: {album.ars_name}")
            with container:
                charts.spotifyProfilePicture(album.ars_name, custom_width=200)

            st.write(f"Album: {album.album}")
            st.write(f"Release Date: {album.rel_date}")
            st.write(f"Genres: {album.gens}")
            st.write(f"Description: {album.descs}")
            st.write(f"Average Rating: {album.avg_rat}")
            st.write(f"Duration (ms): {album.duration_ms}")
            st.write("--------------")

run()
