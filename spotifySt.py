import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import streamlit as st


# Credential'e do mojego konta
CLIENT_ID = '6a83e7e8c4e349739f6eea5e960910a0'
CLIENT_SECRET = 'd0ca847d484f4ac08cd8080a8079ddc4'

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def search_track(query):
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return track['preview_url']
    else:
        return None


def search_artist(query,use_custom_width=None):
    result = sp.search(q=query, type='artist', limit=1)
    if result['artists']['items']:
        artist = result['artists']['items'][0]
        if artist['images']:
            image_url = artist["images"][0]["url"]
            if use_custom_width:
                st.image(image_url, caption="Artist Photo", width=use_custom_width)
            else:
                st.image(image_url, caption="Artist Photo", use_column_width=True)
        else:
            st.write("Artist Doesn't have profile picture")
    else:
        st.write("There no such a artist")




def search_albums(query,use_custom_width=None):
    result = sp.search(q=query, type='album', limit=1)
    albums = result['albums']['items']
    if albums:
        album = albums[0]
        image_url = album['images'][0]['url']
        if use_custom_width:
            st.image(image_url, caption="Album Photo", width=use_custom_width)
        else:
            st.image(image_url, caption="Album Photo", use_column_width=True)
    else:
        st.write("There is no Album photo")
