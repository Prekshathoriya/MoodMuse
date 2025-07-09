# playlist/spotify_recommender.py
from dotenv import load_dotenv
load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

# Emotion to Genre Mapping
EMOTION_GENRE_MAP = {
    "joy": ["pop", "dance", "edm"],
    "sadness": ["acoustic", "indie", "lo-fi"],
    "anger": ["rock", "metal", "trap"],
    "fear": ["ambient", "instrumental", "chill"],
    "love": ["romantic", "r&b", "soul"],
    "surprise": ["party", "hip-hop", "bollywood"],
    "neutral": ["chill", "lo-fi", "instrumental"]
}

def get_genres_for_emotion(emotion):
    return EMOTION_GENRE_MAP.get(emotion.lower(), ["pop"])

# Setup Spotify API
def setup_spotify():
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise Exception("Spotify credentials not found in environment variables.")

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(auth_manager=auth_manager)

# Get recommended playlists based on emotion
def get_playlists_for_emotion(emotion):
    sp = setup_spotify()
    genres = get_genres_for_emotion(emotion)
    playlists = []

    for genre in genres:
        try:
            results = sp.search(q=f"{genre} mood", type="playlist", limit=3)
            items = results.get('playlists', {}).get('items', [])
            for item in items:
                if item and item.get('name') and item.get('external_urls'):
                    playlists.append({
                        "name": item['name'],
                        "url": item['external_urls']['spotify']
                    })
        except Exception as e:
            print(f"Error searching for genre '{genre}': {e}")
    
    return playlists

# Run this file directly to test
if __name__ == "__main__":
    emotion = "joy"
    print(f"For emotion '{emotion}', suggested genres: {get_genres_for_emotion(emotion)}\n")

    playlists = get_playlists_for_emotion(emotion)
    if playlists:
        for p in playlists:
            print(f"{p['name']} ➤ {p['url']}")
    else:
        print("No playlists found.")
