import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Credential'e do mojego konta
CLIENT_ID = '6a83e7e8c4e349739f6eea5e960910a0'
CLIENT_SECRET = '608d827dea6d471587f50cc9f9f4932b'

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def search_track(query):
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return track['preview_url']
    else:
        return None
