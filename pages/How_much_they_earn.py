import pandas as pd
import streamlit as st
import charts

st.set_page_config(layout='wide')

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"\n[FAILED] path '{path}' doesn't exist!")

def runner():
    data = load_data("csvs/artists_data.csv")
    st.title("All-time most streamed artists")

    data_1 = data.groupby('artist')['lead Streams']
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        with st.expander(label="All-time most streamed artists", expanded=True):
            tab1, tab2 = st.tabs(["📈 Bar Chart", "🗃 Data"])
            with tab1:
                charts.most_streamed_artists(data)
            tab2.dataframe(data_1)

    data_2 = data.groupby('artist')['feat Streams']
    with col2:
        with st.expander(label="Feat streams of All-time most streamed artists", expanded=True):
            tab1, tab2 = st.tabs(["📈 Bar Chart", "🗃 Data"])
            with tab1:
                charts.feats_most_streamed_artists(data)
            tab2.dataframe(data_2)

    data_3 = data.groupby('artist')['songs over 1B']
    col5, col6 = st.columns(2, gap="medium")
    with col5:
        with st.expander(label="Songs with over 1 Bilion streams", expanded=True):
            tab1, tab2 = st.tabs(["📈 Bar Chart", "🗃 Data"])
            with tab1:
                charts.songs_over_1B(data)
            tab2.dataframe(data_3)
    data_4 = data.groupby('artist')['songs over 100m']
    with col6:
        with st.expander(label="Songs with over 100 Million streams", expanded=True):
            tab1, tab2 = st.tabs(["📈 Bar Chart", "🗃 Data"])
            with tab1:
                charts.songs_over_100m(data)
            tab2.dataframe(data_4)

    data_5 = data.groupby('artist')['songs over 10m']
    col7, col8 = st.columns(2, gap="medium")
    with col7:
        with st.expander(label="Songs with over 10 Million streams", expanded=True):
            tab1, tab2 = st.tabs(["📈 Bar Chart", "🗃 Data"])
            with tab1:
                charts.songs_over_10m(data)
            tab2.dataframe(data_5)
    data_6 = data.groupby('artist')['tracks recorded']
    with col8:
        with st.expander(label="All track recorded by artist", expanded=True):
            tab1, tab2 = st.tabs(["📈 Bar Chart", "🗃 Data"])
            with tab1:
                charts.tracks_recorded(data)
            tab2.dataframe(data_6)

    data_7 = data.groupby('artist')['lead Streams']
    col3, col4 = st.columns(2, gap="medium")

    with col3:
        with st.expander(label="How much artists made?", expanded=True):
            tab1, tab2 = st.tabs(["📈 Bar Chart", "🗃 Data"])
            with tab1:
                charts.most_streamed_money_maker(data, type_of_chart="bar")
            tab2.dataframe(data_7)

    with col4:
        with st.expander(label="Pie chart of how much artist made from lead streams", expanded=True):
            charts.most_streamed_money_maker(data, type_of_chart="pie")

runner()