from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, Select, String, Boolean, select
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

@app.route("/random")
def get_random_cafe():
    all_cafes = db.session.execute(Select(Cafe))
    all_cafes = all_cafes.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.execute(Select(Cafe))
    all_cafes = all_cafes.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search")
def get_cafe_by_location():
    location = request.args["loc"]
    find_cafe = db.session.execute(Select(Cafe).where(Cafe.location == location))
    cafe = find_cafe.scalar()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

@app.route("/add", methods=["POST"])
def add_cafe():
    data = request.form
    db.session.add(Cafe(
        name=data["name"],
        map_url=data["map_url"],
        img_url=data["img_url"],
        location=data["location"],
        seats=data["seats"],
        has_toilet=bool(data["has_toilet"]),
        has_wifi=bool(data["has_wifi"]),
        has_sockets=bool(data["has_sockets"]),
        can_take_calls=bool(data["can_take_calls"]),
        coffee_price=data["coffee_price"],
    ))
    db.session.commit()
    return jsonify(respose={"success": "Successfully added the new cafe."})

@app.route("/update-price/<int:id>", methods=["PATCH"])
def update_cafe_price(id):
    new_price = request.args["new_price"]
    cafe = db.session.get(Cafe, id)
    if not cafe:
        return jsonify(error={"Not Found": f"Sorry a cafe with id {id} was not find in the database."}), 404
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify({"success":"Successfully updated the price."}), 200

@app.route("/report-closed/<int:id>", methods=["DELETE"])
def delete_cafe(id):
    api_key = request.args["api-key"]
    if api_key != "TopSecretAPIKey":
        return jsonify({"error": f"Sorry, that's not allowed. Your api_key {api_key} is not the expected api_key."})
    cafe = db.session.get(Cafe, id)
    if not cafe:
        return jsonify(error={"Not Found": f"Sorry a cafe with the id {id} was not found in the database."})
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"Success": f"Cafe with id {id} has been deleted."})
    

if __name__ == '__main__':
    app.run(debug=True)
