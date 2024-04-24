import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100"

class MusicScraper:
    """This class is responsible for scraping data from the billboard webpage."""
    def __init__(self) -> None:
        pass

    def search_songs(self, date: str) -> list[str]:
        response = requests.get(url=f"{URL}/{date}/")
        response.raise_for_status()

        website_html = BeautifulSoup(response.text, "html.parser")
        song_tags = website_html.select("#title-of-a-story.a-no-trucate")

        titles = []
        for tag in song_tags:
            title = self.name_formatter(tag.get_text())
            titles.append(title)

        return titles

    def name_formatter(self, text: str) -> str:
        """Remove the extra spaces of a song name."""
        words = text.split()
        length = len(words)

        new_name = ""
        i = 0
        while i < length:
            new_name += words[i]

            if i < length-1:
                new_name += " "

            i += 1

        return new_name
