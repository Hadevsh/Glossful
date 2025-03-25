from flask import Blueprint, render_template, jsonify, request
import os
import json

from app.utils import get_wiktionary_data

main = Blueprint('main', __name__)

# All sub-page routes
@main.route("/")
def home():
    return render_template("index.html")

@main.route("/flashcards")
def flashcards():
    return render_template("flashcards.html")

@main.route("/grammar")
def grammar():
    return render_template("grammar.html")

# New API endpoint to fetch Wiktionary data
@main.route("/api/word/<word>")
def api_word(word):
    result = get_wiktionary_data(word)
    return jsonify(result)

"""
Routes TODO:
--------------------------------------------------

@main.route("/topics")
def topics():
    return render_template("topics.html")

@main.route("/reading")
def reading():
    return render_template("reading.html")

@main.route("/api/vocab/<lang>/<level>")
def vocab_api(lang, level):
    path = os.path.join("app", "data", f"{lang}_{level}.json")
    with open(path, encoding='utf-8') as f:
        words = json.load(f)
    return jsonify(words)
"""
