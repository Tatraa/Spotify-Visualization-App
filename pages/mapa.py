import pandas as pd
import plotly.express as px
import pycountry as pycountry
import streamlit as st

# Wczytaj dane z pliku CSV
import plotly.graph_objects as go

st.set_page_config(layout='wide')


@st.cache_data
def load_data(path:str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        st.write("Nie ma pliku CSV potrzbnego do mapy nalezy wypakowac - nazwac charts.csv")
        print(f"\n[FAILED] path '{path}' doesn't exist!")

@st.cache_data
def load_map(df):
    country_codes = {}
    for country in pycountry.countries:
        country_codes[country.alpha_2.lower()] = country.alpha_3

    df['country_code'] = df['country'].map(country_codes)
    df_mean = df.groupby('country_code')['streams'].mean().reset_index()

    fig = go.Figure(data=go.Choropleth(
        locations=df_mean['country_code'],
        z=df_mean['streams'],
        text=df_mean['country_code'],
    ))

    fig.update_geos(
        showcountries=True,
        countrycolor="gray",
        showcoastlines=True,
        coastlinecolor="white",
        showland=True,
        landcolor="lightgreen",
        bgcolor="lightblue"  # Zmiana koloru tła samej mapy na "lightblue"
    )

    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        annotations=[dict(
            x=0.5,
            y=-0.1,
            xref='paper',
            yref='paper',
            text='Źródło: Dane streamów',
            showarrow=False
        )],
        height=800 ,
        width=800,
        plot_bgcolor='lightblue'
    )

    st.plotly_chart(fig,theme=None,use_container_width=True)

def website_layout():
    st.header("Mapa Pokazująca ilość streamów - wyświetlen w zależnosci od kraju")
    df = load_data('csvs/charts.csv')
    #df = df[0:200000]
    with st.expander(label='Średnia liczba streamów na kraj',expanded=True):
        load_map(df)

website_layout()

# Poprzednia wersja
# fig1 = px.choropleth(df_mean, color="streams",
#                     locations="country_code", projection="natural earth"
#                    )
# fig1.update_geos(
#     showcountries=True,
#     countrycolor="gray",
#     showcoastlines=True,
#     coastlinecolor="white",
#     showland=True,
#     landcolor="lightgray",
#     oceancolor="lightblue"  # Ustawienie koloru oceanów na niebieski
# )0
#
# fig1.update_layout(
#     margin=dict(l=0, r=0, t=0, b=0)  # Usunięcie marginesów wokół mapy
# )


