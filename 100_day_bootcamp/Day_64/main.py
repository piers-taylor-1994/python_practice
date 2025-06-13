from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

class EditMovieForm(FlaskForm):
    rating = FloatField('Your rating out of 10', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Done')

def search_movies(title):
    url = "https://api.themoviedb.org/3/search/movie"
    token = os.environ["API_TOKEN"]

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers, params={"query": title, "language": "en-UK"})
    results = response.json()["results"]
    return [{"id": r["id"], "title": r["original_title"], "date": r["release_date"]} for r in results]

def search_movie(id):
    url = f"https://api.themoviedb.org/3/movie/{id}"
    token = os.environ["API_TOKEN"]

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers, params={"language": "en-UK"})
    results = response.json()
    return {"title": results["original_title"], "img_url": results["poster_path"], "year": results["release_date"], "description": results["overview"]}

# movies = search_movies("Matrix")
# for m in movies:
#     if m["id"] == 555879:
#         print(m)

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(desc(Movie.rating)))
    all_movies = result.scalars().all()
    for movie in all_movies:
        movie.ranking = all_movies.index(movie) + 1
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get("id")
    movie = db.get_or_404(Movie, id)
    edit_form = EditMovieForm(
        rating=movie.rating,
        review=movie.review
    )
    if edit_form.validate_on_submit():
        movie.rating = edit_form.rating.data
        movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=edit_form)

@app.route("/delete")
def delete():
    id = request.args.get("id")
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddMovieForm()
    if add_form.validate_on_submit():
        movies = search_movies(add_form.title.data)
        return render_template("select.html", movies=movies)
        # db.session.add(movie)
        # db.session.commit()
        # return redirect(url_for("edit"))
    return render_template("add.html", form=add_form)

@app.route("/find")
def add_film_from_db():
    id = request.args.get("id")
    movie = search_movie(id)
    db.session.add(Movie(
        id = id,
        title = movie["title"],
        year = movie["year"],
        description = movie["description"],
        rating = None,
        ranking = None,
        review = None,
        img_url = "https://image.tmdb.org/t/p/w500" + movie["img_url"],
    ))
    db.session.commit()
    return redirect(url_for("edit", id=id))

if __name__ == '__main__':
    app.run(debug=True)
