import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

CLIENT_ID = "fc922a4d062748ad909fd0b1e4a24184"
CLIENT_SECRET = "361e028d009c4b5b8e67bfb4cc2993fd"
REDIRECT_URI = "https://example.com"

year = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD: \n")

site = requests.get(f"https://www.billboard.com/charts/hot-100/{year}/", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}).text

soup = BeautifulSoup(site, "html.parser")
# song_titles = [s.getText().split() for s in soup.find_all(name="h3", id="title-of-a-story")]
# song_titles = [s.getText().replace("\n", "").replace("\t", "") for s in soup.select("li ul li #title-of-a-story")]
# song_titles = [" ".join(s.getText().split()) for s in soup.select("li ul li #title-of-a-story")]
song_titles = [s.getText().strip() for s in soup.select("li ul li #title-of-a-story")]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        CLIENT_ID, 
        CLIENT_SECRET, 
        REDIRECT_URI, 
        scope="playlist-modify-private",
        cache_path="Day_46/.cache"
    )
)

user_id = sp.current_user()["id"]

track_list = []

for song in song_titles:
    try:
        track_list.append(sp.search(f"track: {song} year: {year[:4]}")["tracks"]["items"][0]["uri"])
    except:
        with open("Day_46/error_logs.txt", "a") as file:
            file.write(f"Cannot find song {song}\n")

playlist_id = sp.user_playlist_create(user_id, f"{year} Billboard 100", public=False, collaborative=False, description='')["id"]

result = sp.playlist_add_items(playlist_id, track_list)