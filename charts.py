import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import pandas as pd
from spotifySt import search_track, search_artist
from spotifySt import *


def spotifyPlayer(song_title):
    # Spotify Snippet Player
    query = song_title
    if query:
        preview_url = search_track(query)
        if preview_url:
            st.audio(preview_url)
        else:
            st.error('There is no such a song.')

def spotifyProfilePicture(artist_title):
    query = artist_title
    if query:
        image_url = search_artist(query)
        if image_url:
            st.image(image_url)
        else:
            return None


def chart_popularity_genre(data):
    # A chart depicting the relationship between 'top genre'  and 'Popularity'
    fig_popularity_genre = px.bar(data_frame=data,
                                  x='top genre',
                                  y='pop',
                                  title='Chart Showing the Relationship Between Music Genre and Its Popularity'.capitalize(),
                                  color='top genre',
                                  width=1300,
                                  height=600,
                                  log_y=True
                                  )

    fig_popularity_genre.update_layout(
        xaxis={'title': '', 'tickfont': {'size': 13}, 'tickangle': 60},
        yaxis={'title': 'Popularity', 'tickfont': {'size': 17}}
    )

    number_of_unique_values = data['pop'].nunique() - 21
    top_values = st.slider(min_value=3, max_value=number_of_unique_values, value=50, step=1,
                           label="")
    fig_popularity_genre.update_layout(
        xaxis={'title': '', 'range': [1, top_values, ], 'tickfont': {'size': 13}, 'tickangle': 60},
        yaxis={'title': 'Popularity', 'tickfont': {'size': 17}}
    )
    st.plotly_chart(fig_popularity_genre, theme=None)


def chart_bpm_year(data):
    # A chart depicting the relationship between 'Year'  and 'BPM'
    df_mean_bpm = data.groupby('year')['bpm'].mean().reset_index()
    fig_bpm_year = px.bar(data_frame=df_mean_bpm,
                          x='year',
                          y='bpm',
                          title='Chart Showing Average Tempo of Songs by Year',
                          color='bpm'
                          )

    fig_bpm_year.update_layout(
        xaxis={'title': '', 'tickfont': {'size': 13}},
        yaxis={'title': 'BPM', 'tickfont': {'size': 17}}
    )

    return st.plotly_chart(fig_bpm_year, theme=None, use_container_width=True), df_mean_bpm


def chart_genre_nrgy(data):
    # A chart depicting the relationship between 'top genre' and 'energy'
    df_mean_nrgy = data.groupby('top genre')['nrgy'].mean().reset_index()
    fig_genre_nrgy = px.bar(data_frame=df_mean_nrgy,
                            x='top genre',
                            y='nrgy',
                            title='Chart Showing Average Energy of Songs by Their Genre',
                            color='top genre')

    fig_genre_nrgy.update_layout(
        xaxis={'title': '', 'tickfont': {'size': 13}, 'tickangle': 45},
        yaxis={'title': 'ENERGY', 'tickfont': {'size': 17}}
    )

    return st.plotly_chart(fig_genre_nrgy, theme=None, use_container_width=True), df_mean_nrgy


def chart_year_dnce(data):
    df_mean_dnce = data.groupby('year')['dnce'].mean().reset_index()
    fig_year_dnce =  px.bar(data_frame=df_mean_dnce,
                            x='year',
                            y='dnce',
                            title="Chart Showing Average Danceability of Songs by Their year",
                            color='dnce',
                            log_y=True)

    fig_year_dnce.update_layout(
        xaxis={'title': '', 'tickfont': {'size': 13}},
        yaxis={'title': 'DANCEBILITY', 'tickfont': {'size': 17}}
    )
    return st.plotly_chart(fig_year_dnce, theme=None, use_container_width=True), df_mean_dnce

# # TODO:
# # Wykres średniego natężenia dźwięku utworów w zależności od gatunku
# fig5 = px.bar(data_frame=data, x='genre', y='dB', title='Średnie natężenie dźwięku utworów według gatunku')
# # Wykres średniej wartości walencyjnej utworów w zależności od roku
# fig6 = px.bar(data_frame=data, x='year', y='val', title='Średnia wartość walencyjna utworów według roku')
