import pandas as pd
import streamlit as st
import numpy as np
import charts

# !Important
st.set_page_config(layout='wide')

class Song:
    def __init__(self, name, dnce, nrgy, bpm, top_genre,artist):
        self.name = name
        self.dnce = dnce
        self.nrgy = nrgy
        self.bpm = bpm
        self.genre = top_genre
        self.artist = artist

class MusicRecommendationSystem:
    def __init__(self,sensitivity):
        self.songs = []
        self.sensitivity = sensitivity

    def add_song(self, song):
        self.songs.append(song)

    def find_similar_songs(self, selected_song_name):
        similar_songs = []
        selected_song = None

        for song in self.songs:
            if song.name == selected_song_name:
                selected_song = song
                break

        if selected_song is not None:
            for song in self.songs:
                if song != selected_song:
                    similarity_score = self.calculate_similarity(selected_song, song)

                    if similarity_score > self.sensitivity:
                        similar_songs.append(song)

        return similar_songs

    #Metryka Euklidesowa XD , nie sadzilem ze kiedy tego uzyje
    def calculate_similarity(self, song1, song2):
        distance = ((song1.dnce - song2.dnce) ** 2 +
                    (song1.nrgy - song2.nrgy) ** 2 +
                    (song1.bpm - song2.bpm) ** 2)
        similarity = 1 / (1 + distance)
        return similarity

# Data Loader - CSV
@st.cache_data
def load_data(path:str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"\n[FAILED] path '{path}' doesn't exist!")

# Running all stuff on the website
def runner():
    data = load_data("csvs/spotify_2010_2019_data.csv")

    # Sensitivity management
    with st.expander(label="Sensitivity",expanded=False):
        slider = st.slider(min_value=0.0, max_value=1.0, value=0.03, step=0.0001,label_visibility="hidden",label=";")
    recommendation_system = MusicRecommendationSystem(slider)

    # Adding Songs to recommendation system
    for index, row in data.iterrows():
        song = Song(row['title'], row['dnce'], row['nrgy'], row['bpm'], row['top genre'],row['artist'])
        recommendation_system.add_song(song)

    # Streamlit form
    st.title("Music Recommendation System")
    selected_song = st.selectbox("Wybierz utwór:", data['title'])

    if st.button("Znajdź podobne utwory"):
        similar_songs = recommendation_system.find_similar_songs(selected_song)
        if len(similar_songs) > 0:
            st.subheader("Podobne utwory:")

            # Printing Similar songs
            for song in similar_songs:
                st.write(f" TITLE: {song.name}   -----------              ARTIST: {song.artist}")

        else:
            st.write("Brak podobnych utworów")

runner()


