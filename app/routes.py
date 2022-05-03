from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


# planets = [
#     Planet(1, "Arrakis", "A desert planet, source of Spice.", True),
#     Planet(2, "Bela Tegeuse", "The fifth planet of Keuntsing.", False),
#     Planet(3, "Tupile", "Sanctuary planet for defeated houses of the Imperium.", True),
#     Planet(4, "Ix", "Supreme machine culture.", False)
# ]

planets_bp = Blueprint("Planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    all_planets = [
        planet.to_dict()
        for planet in planets
    ]
    return jsonify(all_planets)

@planets_bp.route("", methods=["POST"])
def discover_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        has_moons=request_body["has_moons"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully added to the Planets Database.", 201)

def get_planet_record_by_id(id):
    try:
        id = int(id)
    except ValueError:
        abort(make_response(jsonify(dict(details=f"Invalid id: {id}")),400))
    planet = Planet.query.get(id)
    if planet:
        return planet
    else:
        abort(make_response(jsonify(dict(details=f"Planet id: {id} not found")),404))

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = get_planet_record_by_id(planet_id)
    return jsonify(planet.to_dict())

@planets_bp.route("/<planet_id>", methods=["PUT"])
def replace_planet_by_id(planet_id):
    planet = get_planet_record_by_id(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.has_mooons = request_body["has_moons"]

    db.session.commit()

    return make_response(jsonify(planet.to_dict()))

@planets_bp.route("/<planet_id>", methods=["PATCH"])
def update_planet_by_id(planet_id):
    planet = get_planet_record_by_id(planet_id)

    request_body = request.get_json()
    planet_keys = request_body.keys()
    
    if "name" in planet_keys:
        planet.name = request_body["name"]
    if "description" in planet_keys:
        planet.description = request_body["description"]
    if "has_moons" in planet_keys:
        planet.has_moons = request_body["has_moons"]

    db.session.commit() 
    return make_response(jsonify(planet.to_dict()))

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = get_planet_record_by_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(dict(details=f"Planet {planet.name} successfully deleted from the Planets Database.")))