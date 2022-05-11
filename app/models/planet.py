from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    has_moons = db.Column(db.Boolean, nullable=False)
    moons = db.relationship("Moon", back_populates="planet")
    
    required_attributes = {
        "name":True,
        "description":True,
        "has_moons":True
    }
    # Instance methods:

    def self_to_dict(self):
        list_of_moons = [moon.self_to_dict() for moon in self.moons]
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            has_moons=self.has_moons,
            moons = list_of_moons)
    
    def update_self(self, data_dict):
        for key in data_dict.keys():
            if hasattr(self, key):
                setattr(self, key, data_dict[key])
            else:
                raise ValueError(key)


    # Class methods
    
    @classmethod
    def create_from_dict(cls, data_dict):
        if data_dict.keys() == cls.required_attributes.keys():
            return cls(
            name=data_dict["name"],
            description = data_dict["description"],
            has_moons = data_dict["has_moons"]
        )
        else:
            remaining_keys= set(data_dict.keys())-set(cls.required_attributes.keys())
            response=list(remaining_keys)
            raise ValueError(response)