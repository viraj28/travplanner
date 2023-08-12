from app import app
from flask import render_template, request
from .database import add_contact_data_to_db, load_places_from_db, load_place_from_db, add_itenary_req

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Homepage")

@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact")

@app.route('/explore')
def explore():
    places = load_places_from_db()
    return render_template("explore.html", title="Explore", places = places)

@app.route('/contact/submit', methods=["post"])
def submit_contact():
    data = request.form
    add_contact_data_to_db(data)
    return render_template("contact.html", submitted=True)

@app.route('/get-itenary/<id>', methods=["post", "get"])
def getItenary(id):
    place = load_place_from_db(id)
    if not place:
        return "Not Found", 404
    else:
        return render_template("itenary.html", place=place)
    
@app.route('/itenary/<id>', methods=["post", "get"])
def submit_itenary_req(id):
    data = request.form
    place = load_place_from_db(id)
    if not place:
        return "Not Found", 404
    else:
        add_itenary_req(data, id)
        return render_template('itenary.html', place=place, submitted=True)

