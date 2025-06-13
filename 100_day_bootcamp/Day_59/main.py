from flask import Flask, render_template
import random
import requests
from datetime import *

response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
response.raise_for_status()
blogs = response.json()

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html', img="static/assets/img/home-bg.jpg", title="Clean Blog", subtitle="A Blog Theme by Start Bootstrap", blogs=blogs)

@app.route('/about')
def about_page():
    return render_template('about.html', title="About You", subtitle="An About You section", img="static/assets/img/about-bg.jpg")

@app.route('/contact')
def contact_page():
    return render_template('contact.html', title="Contact", subtitle="A Contact section", img="static/assets/img/contact-bg.jpg")

@app.route('/post/<int:id>')
def post_page(id):
    blog = None
    for b in blogs:
        if b["id"] == id:
            blog = b
    return render_template('post.html', title=blog["title"], subtitle=blog["subtitle"], img=blog["image_url"], id=id, body=blog["body"])

while __name__ == "__main__":
    app.run(debug=True)
