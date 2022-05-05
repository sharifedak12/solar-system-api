import pytest
from app import create_app
from app import db
from app.models.planet import Planet
from flask.signals import request_finished


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def sample_data_with_two_planets(app):
    ocean_planet = Planet(name="Ocean Planet",
                description="It's wet!",
                has_moons=True)
    jungle_planet = Planet(name="Jungle Planet",
                description="Full of big cats. And trees!",
                has_moons=False)

    db.session.add_all([ocean_planet, jungle_planet])
    db.session.commit()