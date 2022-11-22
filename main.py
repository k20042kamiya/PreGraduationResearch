
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    return render_template("index.html", message=None)


@app.route('/voice_recognition', methods=['POST'])
def voice_recognition():
    return render_template("/voice_recognition.html", message=None)


if __name__ == '__main__':
    app.run()
