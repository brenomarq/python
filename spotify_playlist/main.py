from music_scraper import MusicScraper
from playlist_manager import PlaylistManager

music_scraper = MusicScraper()
playlist_manager = PlaylistManager()

chosen_date = input("What year would you like to travel to? (Format: YYYY-MM-DD)\n")

songs = music_scraper.search_songs(chosen_date)
year = chosen_date.split("-")[0]

songs_uri = []
for song in songs:
    name = f"track:{song} year:{year}"

    uri = playlist_manager.search_song(name)
    if uri:
        songs_uri.append(uri)

playlist_name = f"{chosen_date} Billboard 100"
playlist_manager.create_playlist(playlist_name=playlist_name, songs=songs_uri)

