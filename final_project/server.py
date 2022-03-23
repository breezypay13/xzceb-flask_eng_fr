from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")


@app.route("/english_to_french")
def english_to_french():
    # change functions to snake-case and adjust code as shown in translator.py
    text_to_translate = request.args.get('text_to_translate')

    # Write your code here
    return "Translated text to French"


@app.route("/french_to_english")
def french_to_english():
    text_to_translate = request.args.get('text_to_translate')
    # Write your code here
    return "Translated text to English"


@app.route("/")
def render_index_page():

 # Write the code to render template

    if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8080)
