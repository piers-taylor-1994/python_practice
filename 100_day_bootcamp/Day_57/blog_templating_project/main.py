from flask import Flask, render_template
import requests
from post import *

response = requests.get("https://api.npoint.io/2e4d9253f625730f9eb9")
response.raise_for_status()
posts = [Post(p["id"], p["title"], p["subtitle"], p["body"]) for p in response.json()]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/blog/<int:id>')
def get_blog(id):
    requested_post = None
    for post in posts:
        if post.id == id:
            requested_post = post
            break
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
