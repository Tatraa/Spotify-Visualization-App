import requests
import streamlit as st
import spotipy
from spotipy import SpotifyClientCredentials


# Credentials for your Spotify account
CLIENT_ID = '6a83e7e8c4e349739f6eea5e960910a0'
CLIENT_SECRET = '74f51cbd69274031a5d504d670b5bec3'

AUTH_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Obtaining access token
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})
access_token = auth_response.json()['access_token']
headers = {
    'Authorization': f'Bearer {access_token}'
}


def get_available_genres():
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(API_BASE_URL + 'recommendations/available-genre-seeds', headers=headers)
    data = response.json()
    genres = data['genres']
    return genres
def get_top_artists(limit=None, genre=None):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    if genre:
        query = f"year:2022 genre:{genre}"
    else:
        query = "year:2022"

    params = {
        'q': query,
        'type': 'artist',
        'limit': limit
    }

    response = requests.get(API_BASE_URL + 'search', headers=headers, params=params)
    data = response.json()

    if 'artists' not in data:
        return None

    artists = data['artists']['items']
    top_artists = []
    if not artists:
        print("Nie znaleziono żadnego artysty.")
        return top_artists

    for artist in artists:
        ars_name = artist['name']
        genres = artist['genres']
        popularity = artist['popularity']
        image_url = artist['images'][0]['url'] if artist['images'] else None

        top_artists.append({
            'ars_name': ars_name,
            'genres': genres,
            'popularity': popularity,
            'image_url': image_url
        })
    top_artists = sorted(top_artists, key=lambda x: x['popularity'], reverse=True)
    return top_artists



def search_track(query):
    params = {
        'q': query,
        'type': 'track',
        'limit': 1
    }
    response = requests.get(API_BASE_URL + 'search', headers=headers, params=params)
    data = response.json()
    if 'tracks' in data and 'items' in data['tracks'] and data['tracks']['items']:
        track = data['tracks']['items'][0]
        return track['preview_url']
    else:
        return None

def search_artist(query, use_custom_width=None):
    params = {
        'q': query,
        'type': 'artist',
        'limit': 1
    }

    response = requests.get(API_BASE_URL + 'search', headers=headers, params=params)

    data = response.json()
    if 'artists' in data and 'items' in data['artists'] and data['artists']['items']:
        artist = data['artists']['items'][0]
        if artist['images']:
            image_url = artist['images'][0]['url']
            return image_url
        else:
            return None
    else:
        return None

def spotifyProfilePicture(artist_title, custom_width=None):
    query = artist_title
    if query:
        image_url = search_artist(query)
        if image_url:
            if custom_width:
                st.image(image_url, caption='Artist Photo', width=custom_width)
            else:
                st.image(image_url, caption='Artist Photo', use_column_width=True)
        else:
            st.write('There is no profile picture available for this artist.')


def search_albums(query, use_custom_width=None):
    params = {
        'q': query,
        'type': 'album',
        'limit': 1
    }
    response = requests.get(API_BASE_URL + 'search', headers=headers, params=params)
    data = response.json()
    if 'albums' in data and 'items' in data['albums'] and data['albums']['items']:
        albums = data['albums']['items']
        album = albums[0]
        if 'images' in album and album['images']:
            image_url = album['images'][0]['url']
            if use_custom_width:
                st.image(image_url, caption='Album Photo', width=use_custom_width)
            else:
                st.image(image_url, caption='Album Photo', use_column_width=True)
        else:
            st.write('There is no Album photo')
    else:
        st.write('There is no such album')



# from spotipy.oauth2 import SpotifyClientCredentials
# import pandas as pd
# import streamlit as st
#
#
# # Credential'e do mojego konta
# CLIENT_ID = '6a83e7e8c4e349739f6eea5e960910a0'
# CLIENT_SECRET = '74f51cbd69274031a5d504d670b5bec3'
#

#
#
# def search_track(query):
#     results = sp.search(q=query, type='track', limit=1)
#     if results['tracks']['items']:
#         track = results['tracks']['items'][0]
#         return track['preview_url']
#     else:
#         return None
#
#
# def search_artist(query,use_custom_width=None):
#     result = sp.search(q=query, type='artist', limit=1)
#     if result['artists']['items']:
#         artist = result['artists']['items'][0]
#         if artist['images']:
#             image_url = artist["images"][0]["url"]
#             if use_custom_width:
#                 st.image(image_url, caption="Artist Photo", width=use_custom_width)
#             else:
#                 st.image(image_url, caption="Artist Photo", use_column_width=True)
#         else:
#             st.write("Artist Doesn't have profile picture")
#     else:
#         st.write("There no such a artist")
#
#
# def search_albums(query,use_custom_width=None):
#     result = sp.search(q=query, type='album', limit=1)
#     albums = result['albums']['items']
#     if albums:
#         album = albums[0]
#         image_url = album['images'][0]['url']
#         if use_custom_width:
#             st.image(image_url, caption="Album Photo", width=use_custom_width)
#         else:
#             st.image(image_url, caption="Album Photo", use_column_width=True)
#     else:
#         st.write("There is no Album photo")
