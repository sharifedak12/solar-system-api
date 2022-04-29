from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    has_moons = db.Column(db.Boolean, nullable=False)
    
    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            has_moons=self.has_moons)