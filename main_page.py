import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import pandas as pd
from spotifySt import search_track

# IMPORTANT!
st.set_page_config(layout='wide')


@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"\n[FAILED] path '{path}' doesn't exist!")


def home_page(data):
    # Using object notation
    st.title("Home Page")
    chart_data = data[["bpm", "nrgy"]]

    fig = px.scatter(
        chart_data,
        x="bpm",
        y="nrgy",
        size='bpm',
        color="bpm",
        hover_name="bpm",
        log_x=True,
        size_max=160,
        title="Tescior",
        width=1000,
        height=500
    )
    st.plotly_chart(fig, theme=None)

    fig1 = go.Figure(
        data=go.Surface(z=data[["bpm", "nrgy"]]),
        layout=go.Layout(
            title="+100 do zajebistosci",
            width=1000,
            height=800,
        ))
    st.plotly_chart(fig1, theme=None)

    st.header("Bar Chart")
    st.bar_chart(chart_data)



    col1, col2 = st.columns(2, gap="medium")

    with col1:
        with st.expander(label="left", expanded=True):
            tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
            tab1.line_chart(chart_data)
            tab2.dataframe(data)

    with col2:
        with st.expander(label="right", expanded=True):
            tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
            tab1.area_chart(chart_data)
            tab2.dataframe(data)

    container = st.container()

    selected_title = st.selectbox('Wybierz utwór', data['title'])
    with container:
        st.title("Spotify")
        spotifyPlayer(selected_title)


def spotifyPlayer(song_title):
    query = song_title
    if query:
        preview_url = search_track(query)
        if preview_url:
            st.audio(preview_url)
        else:
            st.error('There is no such a song.')


def main():
    data = load_data("csvs/spotify_2010_2019_data.csv")
    home_page(data)


main()
