import os
import asr_streaming_vad as asr
from flask import Flask, request, render_template, jsonify
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


@app.route('/')
def index():
    return render_template("index.html")


# GETメソッド
@app.route('/voice_recognition', methods=["GET"])
def voice_recognition_get():
    state = request.args.get('gs', None)  # ファーストネーム
    print(f'get_state: {state}')
    return asr.main(chunk_size=8000, threshold=45, vad_start=0.3, vad_end=1.0)
    # return render_template("voice_recognition.html")


# POSTメソッド
@app.route('/voice_recognition', methods=["POST"])
def voice_recognition_post():
    state = request.form.get('ps', None)  # ファーストネーム
    print(f'post_state: {state}')
    return render_template("voice_recognition.html")


if __name__ == '__main__':
    app.run()
