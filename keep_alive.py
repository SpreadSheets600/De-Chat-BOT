from flask import Flask
from threading import Thread

app = Flask('Flask Node')


@app.route('/')
def main():
    return "The Bot Is Alive And Is Running"


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    server = Thread(target=run)
    server.start()
