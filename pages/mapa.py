import pandas as pd
import plotly.express as px
import pycountry as pycountry
import streamlit as st

# Wczytaj dane z pliku CSV



@st.cache_data
def load_data(path:str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"\n[FAILED] path '{path}' doesn't exist!")

@st.cache_data
def load_map(df):

    country_codes = {}
    for country in pycountry.countries:
        country_codes[country.alpha_2.lower()] = country.alpha_3

    df['country_code'] = df['country'].map(country_codes)
    df_mean = df.groupby('country_code')['streams'].mean().reset_index()


    fig1 = px.choropleth(df_mean, color="streams",
                        locations="country_code", projection="natural earth"
                       )

    fig1.update_geos(
        showcountries=True,
        countrycolor="gray",
        showcoastlines=True,
        coastlinecolor="white",
        showland=True,
        landcolor="lightgray"
    )


    st.plotly_chart(fig1,theme=None)

df = load_data('csvs/charts.csv')
df = df[0:50000]
load_map(df)




# df['country_code'] = df['country'].map(country_codes)
# print("siema",df)

# # Tworzenie mapy w Plotly
# fig = px.scatter_geo(df, locations="country_code", locationmode='country names',
#                      color='country', projection="natural earth", size="streams")
#



