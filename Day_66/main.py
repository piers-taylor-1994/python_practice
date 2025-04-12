from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random():
    if request.method == "GET":
        result = db.session.execute(db.select(Cafe))
        all_cafes = result.scalars().all()
        random_cafe = random.choice(all_cafes)
        random_cafe
        return jsonify(cafe=random_cafe.to_dict())

@app.route("/all", methods=["GET"])
def get_all():
    if request.method == "GET":
        result = db.session.execute(db.select(Cafe))
        all_cafes = result.scalars().all()
        all_cafes_json = [cafe.to_dict() for cafe in all_cafes]
        return jsonify(cafes=all_cafes_json)
    
@app.route("/search", methods=["GET"])
def search_by_location():
    if request.method == "GET":
        location = request.args.get("loc")
        result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
        filtered_cafes = result.scalars().all()
        if not filtered_cafes:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
        filtered_cafes_json = [cafe.to_dict() for cafe in filtered_cafes]
        return jsonify(cafes=filtered_cafes_json)


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    if request.method == "POST":
        form = request.form
        db.session.add(Cafe(
            name=form["name"],
            map_url=form["map_url"],
            img_url=form["img_url"],
            location=form["location"],
            seats=form["seats"],
            has_toilet=bool(form["has_toilet"]),
            has_wifi=bool(form["has_wifi"]),
            has_sockets=bool(form["has_sockets"]),
            can_take_calls=bool(form["can_take_calls"]),
            coffee_price=form["coffee_price"]
        ))
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
    
# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    try:
        cafe = db.get(Cafe, cafe_id)
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200


# HTTP DELETE - Delete Record
# Deletes a cafe with a particular id. Change the request type to "Delete" in Postman
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        try:
            cafe = db.get(Cafe, cafe_id)
        except AttributeError:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
