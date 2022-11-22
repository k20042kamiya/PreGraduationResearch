import os
from flask import Flask, request, render_template, send_from_directory, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    return render_template("index.html", message=None)


@app.route('/voice_recognition', methods=['POST'])
def voice_recognition():  # 音声認識
    return render_template("voice_recognition.html", message=None)


if __name__ == '__main__':
    app.run()
