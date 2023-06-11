import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import pandas as pd
from spotifySt import search_track,search_artist
import charts
from PIL import Image

# IMPORTANT!
st.set_page_config(layout='wide')


@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"\n[FAILED] path '{path}' doesn't exist!")


def home_page(data,data1):
    # Using object notation
    #
    # #Testowy Wykres
    # st.title("Home Page")
    # chart_data = data1[["tracks recorded", "feat Streams","artist"]]
    # #Testowy Wykres
    # #data = go.Surface(z=data1[["tracks recorded", "feat Streams", "artist"]]),
    # fig1 = go.Figure(
    #     data=go.Surface(z=data1[["feat Streams","lead Streams"]],
    #                     x=data1[["songs over 1m","songs over 10m"]]),
    #     layout=go.Layout(
    #         title="+100 do zajebistosci",
    #         width=1000,
    #         height=800,
    #
    #
    #     ))
    #
    #
    # st.plotly_chart(fig1, theme=None)
    #
    # #-------------#


    # CHART depicting the relationship between 'top genre'  and 'Popularity'
    with st.expander(label="", expanded=True):
        charts.chart_popularity_genre(data)

    # Declaring Layout
    col1, col2 = st.columns(2, gap="medium")

    # A chart depicting the relationship between 'Year'  and 'BPM'
    with col1:
        with st.expander(label="", expanded=True):

            tab1, tab2, tab3, tab4, tab5 = st.tabs(["📈 Bar Chart", "📈 Line Chart", "📈 Area Chart", "📈 Scatter Chart","🗃 Data",])
            with tab1:
                chart, chart_data_df = charts.chart_bpm_year(data)
            with tab2:
                chart, chart_data_df = charts.chart_bpm_year(data,type_of_chart="line")
            with tab3:
                charts.chart_bpm_year(data,type_of_chart="area")
            with tab4:
                chart, chart_data_df = charts.chart_bpm_year(data,type_of_chart="scatter")
            tab5.dataframe(chart_data_df)


    # A chart depicting the relationship between 'top genre' and 'energy'
    with col2:
        with st.expander(label="", expanded=True):
            tab1, tab2, tab3, tab4, tab5 = st.tabs(["📈 Bar Chart", "📈 Line Chart", "📈 Area Chart", "📈 Scatter Chart","🗃 Data",])
            with tab1:
                chart, chart_data_df = charts.chart_genre_nrgy(data)
            with tab2:
                chart, chart_data_df = charts.chart_genre_nrgy(data, type_of_chart="line")
            with tab3:
                charts.chart_genre_nrgy(data, type_of_chart="area")
            with tab4:
                chart, chart_data_df = charts.chart_genre_nrgy(data, type_of_chart="scatter")
            tab5.dataframe(chart_data_df)

    # Declaring Layout
    col3, col4 = st.columns(2, gap="medium")

    # A chart depicting the relationship between 'dnce' and 'year'
    with col3:
        with st.expander(label="",expanded=True):
            tab1, tab2, tab3, tab4, tab5 = st.tabs(["📈 Bar Chart", "📈 Line Chart", "📈 Area Chart", "📈 Scatter Chart", "🗃 Data", ])
            with tab1:
                chart, chart_data_df = charts.chart_year_dnce(data)
            with tab2:
                chart, chart_data_df = charts.chart_year_dnce(data, type_of_chart="line")
            with tab3:
                charts.chart_year_dnce(data, type_of_chart="area")
            with tab4:
                chart, chart_data_df = charts.chart_year_dnce(data, type_of_chart="scatter")
            tab5.dataframe(chart_data_df)

    # A chart depicting the relationship between 'val' and 'year'
    with col4:
        with st.expander(label="",expanded=True):
            tab1, tab2, tab3, tab4 = st.tabs(["📈 Line Chart", "📈 Area Chart", "📈 Scatter Chart", "🗃 Data", ])
            with tab1:
                chart, chart_data_df = charts.chart_val_year(data)
            with tab2:
                charts.chart_val_year(data, type_of_chart="area")
            with tab3:
                chart, chart_data_df = charts.chart_val_year(data, type_of_chart="scatter")
            tab4.dataframe(chart_data_df)


def main():
    image = Image.open("spotifyLogo.png")
    st.sidebar.image(image, width=50)
    data = load_data("csvs/spotify_2010_2019_data.csv")
    data1 = load_data("csvs/artists_data.csv")
    st.header("Dashboard application showing visualization and analysis of Spotify data")
    st.markdown("Welcome to our Spotify Data Analysis website! Here, we dive deep into the world of music to uncover fascinating insights and trends using Spotify's vast collection of data. Our goal is to provide you with an interactive platform that showcases various charts, graphs, and visualizations, highlighting different aspects of songs, as well as recognizing the most popular artists and albums. Through our carefully curated collection of charts, you can explore and compare metrics such as stream counts, popularity rankings, and listener engagement. Whether you're interested in discovering the top tracks of the week, exploring the rising stars in the music industry, or analyzing the impact of specific genres, our charts will provide you with a comprehensive overview.")
    st.markdown("One of the highlights of our website is the podium of the best artists and albums, showcasing the most influential and successful contributors to the music landscape. These rankings are based on a combination of factors, including total streams, chart positions, and critical acclaim. Keep an eye on this section to stay up-to-date with the latest trends and breakthroughs in the music industry. To further enhance your musical journey, we have developed a powerful search engine that helps you find similar songs based on your preferences. This feature utilizes sophisticated algorithms and machine learning techniques to recommend tracks that align with your taste, ensuring an immersive and personalized listening experience.")
    st.markdown("In addition to exploring the music itself, we also provide valuable insights into the financial aspect of Spotify. We delve into the earnings of artists, revealing how streaming revenue impacts their income and shedding light on the economics of the music industry in the digital age. By understanding the financial dynamics of the platform, you'll gain a comprehensive perspective on the music ecosystem. Last but not least, we offer a captivating map that visualizes Spotify's user base around the world. With this interactive map, you can explore which regions and countries have the highest concentration of Spotify listeners, giving you a glimpse into the global reach and impact of the platform.")
    st.markdown("We're thrilled to have you here and hope you enjoy your exploration of Spotify's data-rich world. Whether you're a music enthusiast, industry professional, or data enthusiast, our website aims to deliver an engaging and informative experience. So, sit back, relax, and let the numbers guide your musical adventure!")
    home_page(data,data1)



main()
