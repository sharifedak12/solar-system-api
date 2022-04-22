from crypt import methods
from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, has_moons):
        self.id = id
        self.name = name
        self.desciption = description
        self.has_moons = has_moons
    
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
        dict(
            id = planet.id,
            name = planet.name,
            description = planet.desciption,
            has_moons = planet.has_moons
        )for planet in planets
    ]
    return jsonify(all_planets)