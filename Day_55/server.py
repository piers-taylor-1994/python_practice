from flask import Flask
import random

LOWER_LIMIT = 0
UPPER_LIMIT = 9
RANDOM_NUMBER = random.randint(LOWER_LIMIT, UPPER_LIMIT)

app = Flask(__name__)

@app.route('/')
def home_page():
    return f"<h1>Guess a number between {LOWER_LIMIT} and {UPPER_LIMIT}</h1>" \
    f"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > RANDOM_NUMBER:
        return f"<h1>Too high, try again!</h1>" \
        f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif guess < RANDOM_NUMBER:
        return f"<h1>Too low, try again!</h1>" \
        f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return f"<h1>You found me!</h1>" \
        f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)