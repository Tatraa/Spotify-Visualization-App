import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import pandas as pd
from spotifySt import search_track
import charts

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

    #Testowy Wykres
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

    #Testowy Wykres
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
    
    #-------------#
    st.title("Gotowe Wykresy")

    # CHART depicting the relationship between 'top genre'  and 'Popularity'
    with st.expander(label="", expanded=True):
        charts.chart_popularity_genre(data)

    # Declaring Layout
    col1, col2 = st.columns(2, gap="medium")

    # A chart depicting the relationship between 'Year'  and 'BPM'
    with col1:
        with st.expander(label="", expanded=True):
            tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
            with tab1:
                chart, chart_data_df = charts.chart_bpm_year(data)
            tab2.dataframe(chart_data_df)

    # A chart depicting the relationship between 'top genre' and 'energy'
    with col2:
        with st.expander(label="", expanded=True):
            tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
            with tab1:
                char, chart_data_df = charts.chart_genre_nrgy(data)
            tab2.dataframe(chart_data_df)

    # Declaring Layout
    col3, col4 = st.columns(2, gap="medium")

    with col3:
        with st.expander(label="",expanded=True):
            tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
            with tab1:
                char, chart_data_df = charts.chart_year_dnce(data)
            tab2.dataframe(chart_data_df)

    # TODO 1) - style spotify player   2) - do batter layout
    # Spotify Snippet Player
    container = st.container()
    selected_title = st.selectbox('Wybierz utwór', data['title'])
    with container:
        st.title("Spotify")
        charts.spotifyPlayer(selected_title)


def main():
    data = load_data("csvs/spotify_2010_2019_data.csv")
    home_page(data)


main()
