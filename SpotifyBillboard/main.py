import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ---------------- Spotify Credentials ---------------- #
SPOTIFY_CLIENT_ID="ba9798638e914589881aaaae79e1beb5"
SPOTIFY_CLIENT_SECRET="b0edf0f107fb459ab0d013e20807b90a"
SPOTIFY_REDIRECT_URI = "https://example.com/callback"

# ---------------- User Input ---------------- #
date = input("Which date do you want to travel to? (YYYY-MM-DD): ")
year = date.split("-")[0]

# ---------------- Scrape Billboard ---------------- #
URL = f"https://appbrewery.github.io/bakeboard-hot-100/{date}"

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

songs = [
    song.get_text(strip=True)
    for song in soup.find_all("h3", class_="chart-entry__title")
]

print(f"Found {len(songs)} songs.")

# ---------------- Spotify Authentication ---------------- #
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope="playlist-modify-private",
        show_dialog=True
    )
)

user_id = sp.current_user()["id"]

# ---------------- Search Songs ---------------- #
song_uris = []

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    tracks = result["tracks"]["items"]

    if tracks:
        song_uris.append(tracks[0]["uri"])
        print(f"✓ Found: {song}")
    else:
        print(f"✗ Couldn't find: {song}")

print(f"\nFound {len(song_uris)} songs on Spotify.")

# ---------------- Create Playlist ---------------- #
playlist = sp.current_user_playlist_create(
    name=f"{date} Billboard 100",
    public=False,
    description=f"Billboard Hot 100 from {date}"
)

# ---------------- Add Songs ---------------- #
if song_uris:
    sp.playlist_add_items(
        playlist_id=playlist["id"],
        items=song_uris
    )

print("\nPlaylist created successfully!")
print(f"Playlist name: {playlist['name']}")
print(f"Playlist URL: {playlist['external_urls']['spotify']}")

