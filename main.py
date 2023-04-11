from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG)

# Game state
game_state = {"word": "", "display": "", "guessed_letters": set()}


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


def update_display():
    """Update the display based on guessed letters."""
    global game_state
    game_state["display"] = "".join(
        [
            letter if letter in game_state["guessed_letters"] else "_"
            for letter in game_state["word"]
        ]
    )
    logging.debug(
        f"Display updated to {json.dumps(game_state, indent=2, default=set_default)}"
    )


@app.route("/start_game", methods=["POST"])
def start_game():
    global game_state
    word = request.json.get("word")
    if not word:
        return jsonify({"error": "Word is required"}), 400
    logging.debug(f"Starting game with word {word}")
    game_state["word"] = word.lower()
    game_state["guessed_letters"] = set()
    update_display()
    return jsonify({"message": "Game started", "display": game_state["display"]})


@app.route("/guess_letter", methods=["POST"])
def guess_letter():
    global game_state
    letter = request.json.get("letter")
    if not letter:
        return jsonify({"error": "Letter is required"}), 400
    logging.debug(f"Guessing letter {letter}")
    letter = letter.lower()
    correct_guess = letter in game_state["word"]
    game_state["guessed_letters"].add(letter)
    update_display()
    return jsonify({"correct_guess": correct_guess, "display": game_state["display"]})


@app.route("/guess_whole_word", methods=["POST"])
def get_word():
    global game_state
    word = request.json.get("guessed_word")
    if not word:
        return jsonify({"error": "Word is required"}), 400
    if word.lower() == game_state["word"]:
        return jsonify({"correct_guess": True})


@app.route("/get_display", methods=["GET"])
def get_display():
    global game_state
    return jsonify({"display": game_state["display"]})


@app.route("/.well-known/ai-plugin.json")
def serve_ai_plugin():
    return send_from_directory(".well-known", "ai-plugin.json")


@app.route("/openapi.yaml")
def serve_openai_yaml():
    return send_from_directory(".", "openapi.yaml")


@app.route("/logo.png")
def serve_logo():
    return send_from_directory(".", "logo.png")


if __name__ == "__main__":
    app.run(debug=True, port=3333)
