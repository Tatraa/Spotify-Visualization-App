import pandas as pd
import streamlit as st
import numpy as np
import charts

# !Important
st.set_page_config(layout='wide')


class Song:
    def __init__(self, name, dnce, nrgy, bpm, top_genre, artist):
        self.name = name
        self.dnce = dnce
        self.nrgy = nrgy
        self.bpm = bpm
        self.genre = top_genre
        self.artist = artist
        self.similarity = None


class MusicRecommendationSystem:
    def __init__(self, sensitivity):
        self.distance = None
        self.songs = []
        self.sensitivity = sensitivity
        self.selected_song = None

    def add_song(self, song):
        self.songs.append(song)

    def find_similar_songs(self, selected_song_name,get_selected_song=False):
        similar_songs = []
        selected_song = None

        #return Song selected by user
        if get_selected_song:
            for song in self.songs:
                if song.name == selected_song_name:
                    self.selected_song = song
                    break
            return self.selected_song

        #Calculate Similar songs
        else:
            for song in self.songs:
                if song.name == selected_song_name:
                    selected_song = song
                    break

            if selected_song is not None:
                for song in self.songs:
                    if song != selected_song:
                        similarity_score = self.calculate_similarity(selected_song, song)
                        song.similarity = similarity_score
                        if similarity_score > self.sensitivity:
                            similar_songs.append(song)

            return similar_songs

    # Metryka Euklidesowa XD , nie sadzilem ze kiedy tego uzyje
    def calculate_similarity(self, song1, song2):
        self.distance = ((song1.dnce - song2.dnce) ** 2 +
                         (song1.nrgy - song2.nrgy) ** 2 +
                         (song1.bpm - song2.bpm) ** 2)
        similarity = 1 / (1 + self.distance)
        return similarity

    def get_similarity(self):
        return self.distance


# Data Loader - CSV
@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"\n[FAILED] path '{path}' doesn't exist!")


# Running all stuff on the website
def runner():
    data = load_data("csvs/spotify_2010_2019_data.csv")

    st.title("Music Recommendation System")

    # Sensitivity management
    with st.expander(label="Sensitivity", expanded=False):
        slider = st.slider(min_value=0.0, max_value=1.0, value=0.03, step=0.0001, label_visibility="hidden", label=";")
    recommendation_system = MusicRecommendationSystem(slider)

    # Adding Songs to recommendation system
    for index, row in data.iterrows():
        song = Song(row['title'], row['dnce'], row['nrgy'], row['bpm'], row['top genre'], row['artist'])
        recommendation_system.add_song(song)

    container_for_spotify_player = st.container()

    # Showing Selected Song layout
    with container_for_spotify_player:
        with st.expander(label="Choose a Song",expanded=True):
            selected_song = st.selectbox(label="",label_visibility="hidden", options=data['title'])

            # True option - return just 1 seleted by user song
            chosen_song = recommendation_system.find_similar_songs(selected_song, get_selected_song=True)

            col1, col2 = st.columns([1, 3])
            with col1:
                charts.spotifyProfilePicture(chosen_song.artist)
            with col2:
                container_inside_col2 = st.container()
                with container_inside_col2:
                    st.title(f" {chosen_song.artist} - {chosen_song.name}")
                    st.write("Description 1")
                    st.write("Description 2")
            charts.spotifyPlayer(chosen_song.name)

    #Printing Similar Songs
    if st.button("Find Similar Songs"):
        similar_songs = recommendation_system.find_similar_songs(selected_song)
        if len(similar_songs) > 0:
            st.subheader("Results:")

            # Printing Similar songs using API
            for song in similar_songs:
                with st.expander(label=f"Similarity Indicator - {song.similarity}", expanded=True):
                    col1, col2 = st.columns([1, 3])

                    with col1:
                        charts.spotifyProfilePicture(song.artist)
                    with col2:
                        container_inside_col2 = st.container()
                        with container_inside_col2:
                            st.title(f" {song.artist} - {song.name}")
                            # TODO: Pobrac jakies informacje z API spotify i wypelnic te st.write(), np. ilosc wyświetlen
                            # TODO: Mozna tu wstawic jaki wykres (spider charta) ktory moze obrazowac podobienstwo i ilsoc piosenek
                            st.write("Description 1")
                            st.write("Description 2")
                    charts.spotifyPlayer(song.name)


        else:
            st.write(f"No Similar Songs")


runner()
