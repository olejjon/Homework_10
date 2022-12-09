from flask import Flask

app = Flask(__name__)

@app.route("/")
def page_index():
    return "q"


@app.route('/users/<int:uid>')
def profile(uid):
    return f'Профиль {uid}'


@app.route("/feed/")
def page_feed():
    return "Лента пользователя"

@app.route("/messages/")
def page_messages():
    return "Сообщения пользователя"

app.run(host='0.0.0.0', port=8000)