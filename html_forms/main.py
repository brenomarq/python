from flask import Flask, render_template
from flask import request


app = Flask(__name__)


@app.route('/')
def home() -> str:
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login() -> str:
    data = request.form

    return render_template('login.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
