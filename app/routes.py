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



# @planets_bp.route("/<id>", methods=("GET",))
# def handle_planet(id):
#     planet = validate_planet(id)
#     return jsonify(planet.to_dict())

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         abort(make_response(jsonify(dict(details=f"Planet {planet_id} is invalid!")),400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
    
#     abort(make_response(jsonify(dict(details=f"Planet {planet_id} not found.")),404))