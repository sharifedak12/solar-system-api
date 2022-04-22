from flask import Blueprint

class Planets:
    def __init__(self, id, name, description, has_moons):
        self.id = id
        self.name = name
        self.desciption = description
        self.has_moons = has_moons
    
planets = [
    Planets(1, "Arrakis", "A desert planet, source of Spice.", True),
    Planets(2, "Bela Tegeuse", "The fifth planet of Keuntsing.", False),
    Planets(3, "Tupile", "Sanctuary planet for defeated houses of the Imperium.", True),
    Planets(4, "Ix", "Supreme machine culture.", False)
]