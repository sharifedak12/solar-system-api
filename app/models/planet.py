from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    has_moons = db.Column(db.Boolean, nullable=False)
    moons = db.relationship("Moon", back_populates="planet")
    
    required_attributes = ["name","description","has_moons"]

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
        error_list =[]
        for key in data_dict.keys():
            if hasattr(self, key):
                setattr(self, key, data_dict[key])
            else:
                error_list.append(key)

        if error_list:
            raise ValueError(error_list)


    # Class methods
    
    @classmethod
    def create_from_dict(cls, data_dict):
        keys_list = list(data_dict.keys())
        if keys_list == cls.required_attributes:
            return cls(
            name=data_dict["name"],
            description = data_dict["description"],
            has_moons = data_dict["has_moons"]
        )
        else:
            remaining_keys= set(data_dict.keys())-set(cls.required_attributes)
            response=list(remaining_keys)
            raise ValueError(response)