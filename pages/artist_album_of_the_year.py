import streamlit as st
import pandas as pd
import charts
from spotifySt import *

st.set_page_config(layout='wide')


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


@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"\n[FAILED] path '{path}' doesn't exist!")


def display_album(album):
    with st.expander(label="# Wynik", expanded=True):
        st.write(f"Album: {album.album}")
        st.write(f"Artist: {album.ars_name}")
        st.write(f"Release Date: {album.rel_date}")
        st.write(f"Genres: {album.gens}")
        st.write(f"Description: {album.descs}")
        st.write(f"Average Rating: {album.avg_rat}")
        st.write(f"Duration : {album.duration_ms / 100}")
        image = charts.spotifyProfilePicture(album.ars_name, custom_width=300)
        image2 = charts.spotifyAlbumPicture(album.ars_name, custom_width=300)
        if image is not None and image2 is not None:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(image)
            with col2:
                st.image(image2)
        if image is not None:
            st.image(image)
        if image2 is not None:
            st.image(image2)
        st.write("--------------")


def run():
    data = load_data("csvs/Top5000_album_rating.csv")
    st.title("Top Albums")

    num_albums = st.number_input("Enter the number of albums to display:", min_value=1, max_value=len(data), value=5,
                                 step=1)
    top_albums = []

    for index, row in data.iterrows():
        album = Album(row['ars_name'], row['rel_date'], row['gens'], row['descs'], row['avg_rat'], row['duration_ms'],
                      row['album'])
        album.add_album(album)
        if len(top_albums) < num_albums:
            top_albums.append(album)
        else:
            min_rating = min(top_albums, key=lambda x: x.avg_rat)
            if album.avg_rat > min_rating.avg_rat:
                top_albums.remove(min_rating)
                top_albums.append(album)

    display_albums = []

    for album in top_albums:
        display_albums.append(album)

    with st.container():
        for album in display_albums:
            display_album(album)


run()