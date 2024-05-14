import os
from flask import Flask, render_template
from flask import request
from requests import get
from smtplib import SMTP
from post import Post
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def fetch_posts() -> list[Post]:
    # url to edit data: https://www.npoint.io/docs/087ce95906e07c330408
    posts_url = 'https://api.npoint.io/087ce95906e07c330408'

    response = get(url=posts_url)
    response.raise_for_status()

    posts_data = response.json()
    posts = []
    for post in posts_data:
        current_post = Post(post)
        posts.append(current_post)

    return posts


def send_email(msg_data: dict) -> None:
    email = os.environ.get('EMAIL')
    password = os.environ.get('PASSWORD')

    if email != None and password != None:
        with SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=msg_data['email'],
                to_addrs=email,
                msg=msg_data['message'])


app = Flask(__name__)


@app.route('/')
def home() -> str:
    all_posts = fetch_posts()

    return render_template('index.html', posts=all_posts)


@app.route('/about')
def about() -> str:
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact() -> str:
    if request.method == 'GET':
        return render_template('contact.html', status=False)

    if request.method == 'POST':
        msg_data = request.form

        send_email(msg_data)

        return render_template('contact.html', status=True)

    return 'Error 404'


@app.route('/posts/<int:id>')
def get_post(id: int) -> str:
    all_posts = fetch_posts()

    post: Post = list(filter(lambda post: post.id == id, all_posts))[0]

    return render_template('post.html', post=post)


if __name__ == "__main__":
    app.run(debug=True)
