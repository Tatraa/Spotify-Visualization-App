import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import pandas as pd
from spotifySt import search_track, search_artist
from spotifySt import *


TYPES_OF_ST_CHARTS = ['line','bar','area','scatter','map']

def spotifyPlayer(song_title):
    # Spotify Snippet Player
    query = song_title
    if query:
        preview_url = search_track(query)
        if preview_url:
            st.audio(preview_url)
        else:
            st.write("Player for this song is not available")


def spotifyProfilePicture(artist_title, custom_width=None):
    query = artist_title
    if query:
        if custom_width:
            image_url = search_artist(query, use_custom_width=custom_width)
        else:
            image_url = search_artist(query)

        if image_url:
            st.image(image_url)
        else:
            return None


def spotifyAlbumPicture(album_title, custom_width=None):
    query = album_title
    if query:
        if custom_width:
            image_url = search_albums(query, use_custom_width=custom_width)
        else:
            image_url = search_albums(query)

        if image_url:
            st.image(image_url)
        else:
            return None

def similar_songs_radar_chart(song_object):
    data_dict = {
        "name": [song_object.name],
        "dnce": [song_object.dnce],
        "nrgy": [song_object.nrgy],
        "bpm": [song_object.bpm],
        "genre": [song_object.genre],
        "artist": [song_object.artist],
        "similarity": [song_object.similarity]
    }

    data = pd.DataFrame(data_dict)
    categories = ["dnce", "nrgy", "bpm"]

    # Tworzenie Radar Chart dla każdej kategorii
    fig = go.Figure()

    for index, row in data.iterrows():
        values = row[categories].tolist()
        values += values[:1]

        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories + [categories[0]],
            fill='toself',
            name=row['name']
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True),
        ),
        height=500,
        width=600
    )
    return fig

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


def chart_bpm_year(data,type_of_chart="bar"):
    # A chart depicting the relationship between 'Year'  and 'BPM'
    df_mean_bpm = data.groupby('year')['bpm'].mean().reset_index()
    fig_bpm_year = None

    if type_of_chart in TYPES_OF_ST_CHARTS:
        pass
    else:
        return st.write(f"No such a chart like {type_of_chart}")

    if type_of_chart=="bar":
        fig_bpm_year = px.bar(data_frame=df_mean_bpm,
                              x='year',
                              y='bpm',
                              title='Chart Showing Average Tempo of Songs by Year',
                              color='bpm'
                              )

    elif type_of_chart == "line":
        fig_bpm_year = px.line(data_frame=df_mean_bpm,
                               x='year',
                               y='bpm',
                               title='Chart Showing Average Tempo of Songs by Year',
                               )

    elif type_of_chart == "area":
        return  st.area_chart(data=df_mean_bpm,x='year',y='bpm',use_container_width=True)

    elif type_of_chart=="scatter":
        fig_bpm_year = px.scatter(data_frame=df_mean_bpm,
                                  x='year',
                                  y='bpm',
                                  title='Chart Showing Average Tempo of Songs by Year',
                                  size='bpm',
                                  color='bpm',
                                  log_y=True)

    fig_bpm_year.update_layout(
        xaxis={'title': '', 'tickfont': {'size': 13}},
        yaxis={'title': 'BPM', 'tickfont': {'size': 17}}
    )

    return st.plotly_chart(fig_bpm_year, theme=None, use_container_width=True), df_mean_bpm


def chart_genre_nrgy(data,type_of_chart="bar"):
    # A chart depicting the relationship between 'top genre' and 'energy'
    df_mean_nrgy = data.groupby('top genre')['nrgy'].mean().reset_index()
    fig_genre_nrgy = None

    if type_of_chart in TYPES_OF_ST_CHARTS:
        pass
    else:
        return st.write(f"No such a chart like {type_of_chart}")

    if type_of_chart == "bar":
        fig_genre_nrgy = px.bar(data_frame=df_mean_nrgy,
                                x='top genre',
                                y='nrgy',
                                title='Chart Showing Average Energy of Songs by Their Genre',
                                color='top genre')

    elif type_of_chart == "line":
        fig_genre_nrgy = px.line(data_frame=df_mean_nrgy,
                               x='top genre',
                               y='nrgy',
                                title='Chart Showing Average Energy of Songs by Their Genre',
                               )

    elif type_of_chart == "area":
        return  st.area_chart(data=df_mean_nrgy,x='top genre',y='nrgy',use_container_width=True)

    elif type_of_chart=="scatter":
        fig_genre_nrgy = px.scatter(data_frame=df_mean_nrgy,
                                  x='top genre',
                                  y='nrgy',
                                  title='Chart Showing Average Energy of Songs by Their Genre',
                                  size='nrgy',
                                  color='top genre',
                                  log_y=True)

    fig_genre_nrgy.update_layout(
        xaxis={'title': '', 'tickfont': {'size': 13}, 'tickangle': 45},
        yaxis={'title': 'ENERGY', 'tickfont': {'size': 17}}
    )

    return st.plotly_chart(fig_genre_nrgy, theme=None, use_container_width=True), df_mean_nrgy


def chart_year_dnce(data,type_of_chart="bar"):
    # A chart depicting the relationship between 'dnce' and 'year'
    df_mean_dnce = data.groupby('year')['dnce'].mean().reset_index()

    fig_year_dnce = None

    if type_of_chart in TYPES_OF_ST_CHARTS:
        pass
    else:
        return st.write(f"No such a chart like {type_of_chart}")

    if type_of_chart == "bar":
        fig_year_dnce =  px.bar(data_frame=df_mean_dnce,
                                x='year',
                                y='dnce',
                                title="Chart Showing Average Danceability of Songs by Their year",
                                color='dnce',
                                log_y=True)

    elif type_of_chart == "line":
        fig_year_dnce = px.line(data_frame=df_mean_dnce,
                               x='year',
                               y='dnce',
                               title="Chart Showing Average Danceability of Songs by Their year",
                               )

    elif type_of_chart == "area":
        return  st.area_chart(data=df_mean_dnce,x='year',y='dnce',use_container_width=True)

    elif type_of_chart=="scatter":
        fig_year_dnce = px.scatter(data_frame=df_mean_dnce,
                                  x='year',
                                  y='dnce',
                                  title="Chart Showing Average Danceability of Songs by Their year",
                                  size='dnce',
                                  color='year',
                                  log_y=True)


    fig_year_dnce.update_layout(
        xaxis={'title': '', 'tickfont': {'size': 13}},
        yaxis={'title': 'DANCEBILITY', 'tickfont': {'size': 17}}
    )
    return st.plotly_chart(fig_year_dnce, theme=None, use_container_width=True), df_mean_dnce


def chart_val_year(data,type_of_chart="line"):
    # A chart depicting the relationship between 'val' and 'year'
    df_mean_val = data.groupby('year')['val'].mean().reset_index()
    fig_val_year=None

    if type_of_chart in TYPES_OF_ST_CHARTS:
        pass
    else:
        return st.write(f"No such a chart like {type_of_chart}")

    if type_of_chart == "line":
        fig_val_year = px.line(data_frame=df_mean_val,
                               x='year',
                               y='val',
                               title="Chart Showing Average Danceability of Songs by Their year",
                               )

    elif type_of_chart == "area":
        return  st.area_chart(data=df_mean_val,x='year',y='val',use_container_width=True)

    elif type_of_chart=="scatter":
        fig_val_year = px.scatter(data_frame=df_mean_val,
                                  x='year',
                                  y='val',
                                  title="Chart Showing Average Danceability of Songs by Their year",
                                  size='val',
                                  color='val',
                                  log_y=True)


    fig_val_year.update_layout(
        xaxis={'title': '', 'tickfont': {'size': 13}, 'tickangle': 45},
        yaxis={'title': 'val', 'tickfont': {'size': 17}}
    )

    return st.plotly_chart(fig_val_year, theme=None, use_container_width=True), df_mean_val


def most_streamed_artists(data):

    fig = px.bar(data, x='artist', y='lead Streams',color='artist', title='Lead Stream vs Artysta')

    fig.update_layout(
        xaxis={'title': '', 'tickfont': {'size': 13}, 'tickangle': 45},
        yaxis={'title': 'Streams', 'tickfont': {'size': 17}}
    )
    return st.plotly_chart(fig)
def most_streamed_money_maker(data):

    data["lead Streams"] = data["lead Streams"] * 0.0032
    fig = px.bar(data, x='artist', y='lead Streams',color='artist', title='Lead Stream vs Artysta')

    fig.update_layout(
        xaxis={'title': '', 'tickfont': {'size': 13}, 'tickangle': 45},
        yaxis={'title': 'Money made - USD', 'tickfont': {'size': 17}}
    )
    return st.plotly_chart(fig)

# TODO:
# Wymyslić jeszcze kilka innych wykresów ( innych rodzajów niz bar-chart ) takich zeby dane na nich sie dobrze prezentowały
