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
    st.title("How much they earn?")
    st.markdown("The music industry has undergone a significant transformation with the advent of streaming platforms like Spotify. These platforms have not only revolutionized the way we consume music but also provided artists with new avenues for earning income. Spotify, being one of the leading players in the streaming market, offers a vast collection of songs from various genres, attracting millions of listeners worldwide. As a result, it has become an intriguing subject to analyze the earnings of the top artists on Spotify. In this analysis, we will delve into the data surrounding the earnings of the top 25 streamed artists on Spotify. By examining the financial success of these artists, we can gain insights into the dynamics of the music industry in the digital age. Additionally, we can explore the factors that contribute to an artist's popularity and financial prosperity on this platform.")
    st.markdown("Our objective is to uncover trends, patterns, and correlations within the dataset, allowing us to draw meaningful conclusions about the highest-earning artists on Spotify. We will consider various metrics such as total streams and revenue to provide a comprehensive overview of their success.")
    st.markdown("To accomplish our goal, we will utilize statistical techniques, data visualization, and exploratory data analysis to uncover valuable insights. Through this process, we can identify the most influential factors that contribute to an artist's position within the top 25 earners on Spotify.")

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
    st.markdown(
        "Furthermore, it is important to note that artists earn revenue on Spotify through a complex system that takes into account various factors. One of the key components of an artist's earnings is the payment per stream, which is currently estimated to be around $0.0033 (USD) per play (according to https://eu.usatoday.com/story/life/2022/10/22/how-much-per-spotify-stream/8094437001/). This means that for every song played on the platform, the artist receives a fraction of a cent.While this may seem like a small amount, the cumulative effect of millions or even billions of streams can lead to substantial earnings for the most popular artists. It's worth mentioning that the revenue distribution on Spotify is also influenced by the type of subscription a listener has, with premium subscribers generating higher royalties compared to free users. However, it's essential to consider that an artist's earnings from streaming services like Spotify are just one aspect of their overall income. Artists often derive revenue from other sources such as live performances, merchandise sales, brand endorsements, and licensing deals. These additional revenue streams contribute significantly to an artist's overall financial success and are essential for sustaining their careers.")
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

    st.markdown("Analyzing the earnings of the top 25 artists on Spotify provides valuable insights into the potential financial rewards that can be achieved through streaming platforms. It highlights the immense popularity and influence these artists have within the music industry. Additionally, it underscores the power of streaming services as a source of revenue and exposure for artists, particularly in an era where digital consumption has become the norm. In conclusion, exploring the earnings of the top 25 Spotify artists allows us to gain a better understanding of the financial landscape of the music industry in the streaming era. By considering the payment per stream and its cumulative effect, we can appreciate the significance of streaming platforms in generating revenue for artists. It is an exciting topic to analyze as it offers insights into the dynamics of the music industry and the opportunities available to artists in the digital age")
runner()