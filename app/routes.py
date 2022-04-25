from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, has_moons):
        self.id = id
        self.name = name
        self.desciption = description
        self.has_moons = has_moons
    
    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.desciption,
            has_moons=self.has_moons)

planets = [
    Planet(1, "Arrakis", "A desert planet, source of Spice.", True),
    Planet(2, "Bela Tegeuse", "The fifth planet of Keuntsing.", False),
    Planet(3, "Tupile", "Sanctuary planet for defeated houses of the Imperium.", True),
    Planet(4, "Ix", "Supreme machine culture.", False)
]

planets_bp = Blueprint("Planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=("GET",))
def get_all_planets():
    all_planets = [
        planet.to_dict()
        for planet in planets
    ]
    return jsonify(all_planets)

@planets_bp.route("/<id>", methods=("GET",))
def handle_planet(id):
    planet = validate_planet(id)
    return jsonify(planet.to_dict())

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response(jsonify(dict(details=f"Planet {planet_id} is invalid!")),400))

    for planet in planets:
        if planet.id == planet_id:
            return planet
    
    abort(make_response(jsonify(dict(details=f"Planet {planet_id} not found.")),404))