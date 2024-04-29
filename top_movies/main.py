import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
html_text = response.text

content = BeautifulSoup(html_text, "html.parser")

raw_titles = content.select(".article-title-description__text h3")
titles = [title.get_text() for title in raw_titles][::-1]

with open("movies.txt", "+w", encoding="utf-8") as file:
    for title in titles:
        file.write(f"{title}\n".replace(")", "."))

