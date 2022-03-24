from venv import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")


@app.route("/english_to_french")
def english_to_french():
    # change functions to snake-case and adjust code as shown in translator.py
    text_to_translate = request.args.get('text_to_translate')
    translator1 = english_to_french(text_to_translate)
    return translator1


@app.route("/french_to_english")
def french_to_english():
    text_to_translate = request.args.get('text_to_translate')
    translator1 = french_to_english(text_to_translate)
    return translator1


@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
