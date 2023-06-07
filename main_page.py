import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import pandas as pd
from spotifySt import search_track,search_artist
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
    #Testowy Wykres
    fig1 = go.Figure(
        data=go.Surface(z=data[["bpm", "nrgy"]]),
        layout=go.Layout(
            title="+100 do zajebistosci",
            width=1000,
            height=800,
        ))
    st.plotly_chart(fig1, theme=None)

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
    data = load_data("csvs/spotify_2010_2019_data.csv")
    home_page(data)


main()
