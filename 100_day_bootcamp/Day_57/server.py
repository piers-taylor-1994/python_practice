from flask import Flask, render_template
import random
import requests
from datetime import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template('index.html', num=random_number, year=year)

@app.route('/guess/<name>')
def guess_name(name):
    response = requests.get(f"https://api.genderize.io/?name={name}")
    response.raise_for_status()
    text = response.json()
    gender = text["gender"]
    print(gender)

    response = requests.get(f"https://api.agify.io/?name={name}")
    response.raise_for_status()
    age = response.json()["age"]

    return render_template('guess.html', name="Piers", gender=gender, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response = requests.get(f"https://api.npoint.io/2e4d9253f625730f9eb9")
    response.raise_for_status()
    return render_template('blog.html', posts=response.json())

if __name__ == "__main__":
    app.run(debug=True)