from flask import Blueprint, render_template, jsonify
import json
import os

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("index.html")

"""
@main.route("/flashcards")
def flashcards():
    return render_template("flashcards.html")

@main.route("/topics")
def topics():
    return render_template("topics.html")

@main.route("/grammar")
def grammar():
    return render_template("grammar.html")

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