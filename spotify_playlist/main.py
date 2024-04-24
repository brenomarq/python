from music_scraper import MusicScraper
from playlist_manager import PlaylistManager

music_scraper = MusicScraper()

chosen_year = input("What year would you like to travel to? (Format: YYYY-MM-DD)\n")

for title in music_scraper.search_songs(chosen_year):
    print(title)


