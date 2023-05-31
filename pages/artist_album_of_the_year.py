import streamlit as st
import spotipy
from charts import *
from spotifySt import *

st.set_page_config(layout='wide')
# TODO:
# Filtrowanie po artystach i albumach roku, dołączenie analizy danych - 31.05.2023

class Album:
    def __int__(self, ars_name, rel_date, gens, descs, avg_rat, duration_ms, album):
        self.ars_name = ars_name
        self.rel_date = rel_date
        self.gens = gens
        self.descs = descs
        self.avg_rat = avg_rat
        self.duration_ms = duration_ms
        self.album = album
        self.albums = []

    def add_album(self, album):
        return self.albums.append(album)
@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"\n[FAILED] path '{path}' doesn't exist!")

def run():
    data = load_data("csvs/Top5000_album_rating")
    st.title("Top Albums")

    for index, row in data.iterrows():
        all_albums = Album(row['ars_name'], row['rel_date'], row['gens'], row['descs'], row['avg_rat'], row['duration_ms'], row['album'])
        Album.add_album(all_albums)
run()