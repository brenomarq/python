from flask import Flask, render_template
from datetime import datetime
from requests import get
from post import Post


def fetch_posts() -> list[Post]:
    posts_url = 'https://api.npoint.io/c790b4d5cab58020d391'

    response = get(url=posts_url)
    response.raise_for_status()

    posts_data = response.json()
    posts = []
    for post in posts_data:
        current_post = Post(post)
        posts.append(current_post)


app = Flask(__name__)


@app.route('/')
def home():
    all_posts = fetch_posts()

    return render_template('index.html', year=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
