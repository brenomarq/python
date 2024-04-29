import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

ID = os.environ.get("CLIENT_ID")
SECRET = os.environ.get("CLIENT_SECRET")
URI = "http://example.com"
SCOPE = "playlist-modify-private"

class PlaylistManager:
    def __init__(self) -> None:
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=ID,
            client_secret=SECRET,
            redirect_uri=URI,
            scope=SCOPE,
            show_dialog=True,
            cache_path=".cache"
        ))

        self.user_id = self.sp.current_user()["id"]

    def search_song(self, name: str) -> str | None:
        """Seach for a song and return its uri on spotify."""
        result = self.sp.search(q=name, type="track")

        try:
            uri = result["tracks"]["items"][0]["uri"]
            return uri

        except IndexError:
            return None

    def create_playlist(self, playlist_name: str, songs: list[str]) -> None:
        """Create a playlist on Spotify with all the songs included in the songs list."""
        playlist = self.sp.user_playlist_create(
            user=self.user_id,
            name=playlist_name,
            public=False
        )

        id = playlist["id"]
        self.sp.playlist_add_items(playlist_id=id, items=songs)
