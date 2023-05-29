import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import streamlit as st
'''import base64
from requests import post, get
import json'''

# Credential'e do mojego konta
CLIENT_ID = '6a83e7e8c4e349739f6eea5e960910a0'
CLIENT_SECRET = '608d827dea6d471587f50cc9f9f4932b'

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

'''
# próba innego zalogowanmia do API - nie wyszlo x D
def get_token():
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization" : "Bearer" + token}
def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    print(json_result)

token = get_token()
search_artist(token, "ACDC")
#print(token)
'''



def search_track(query):
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return track['preview_url']
    else:
        return None


def search_artist(query):
    result = sp.search(q=query, type='artist', limit=1)
    if result['artists']['items']:
        artist = result['artists']['items'][0]
        if artist['images']:
            image_url = artist["images"][0]["url"]
            st.image(image_url, caption="Zdjęcie profilowe", width=200)
        else:
            st.write("ziomek nei ma zdjecia")
    else:
        st.write("nie ma takiego ziomka")
'''

def search_artist(query):
    result = sp.search(q=query, type='artist', limit=1)
    if result['artists']['items']:
        artist = result['artists']['items'][0]
        return artist['preview_url']
    else:
        return None
    '''

def search_albums(query):
    result = sp.search(q=query, type='albums', limit=1)
    if result['albums']['items']:
        artist = result['albums']['items'][0]
        return artist['preview_image']
    else:
        return None