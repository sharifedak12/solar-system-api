from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.moon import Moon

moons_bp = Blueprint("Moons", __name__, url_prefix="/moons")

def error_message(message, status_code):
    abort(make_response(jsonify(dict(details=message)), status_code))

def success_message(message, status_code=200):
    return make_response(jsonify(dict(details=message)), status_code)

def return_database_info(return_value):
    return make_response(jsonify(return_value))

def get_moon_record_by_id(id):
    try:
        id = int(id)
    except ValueError:
        error_message(f"Invalid id: {id}", 400)
    moon = Moon.query.get(id)
    if moon:
        return moon
    else:
        error_message(f"Moon id: {id} not found", 404)

def discover_moon_safely(data_dict):
    try:
        return Moon.create_from_dict(data_dict)
    except ValueError as err:
        error_message(f"Invalid key(s):{err}. moon not added to database.", 400)
    except KeyError as err:
        error_message(f"Missing key(s): {err}.  moon not added to database.", 400)


def update_moon_safely(Moon, data_dict):
    try:
        Moon.update_self(data_dict)
    except ValueError as err:
        error_message(f"Invalid key(s): {err}. moon not updated.", 400)
    except KeyError as err:
        error_message(f"Missing key(s): {err}. moon not updated.", 400)




# Route Functions:

@moons_bp.route("", methods=["GET"])
def get_all_moons():
    description_param = request.args.get("description")
    if description_param:
        moons = Moon.query.filter(Moon.description.like('%'+description_param+'%')).all()
    else:
        moons = Moon.query.all()
    
    all_moons = [
        moon.self_to_dict()
        for moon in moons
    ]
    return return_database_info(all_moons)


@moons_bp.route("/<moon_id>", methods=["GET"])
def read_one_moon(moon_id):
    moon = get_moon_record_by_id(moon_id)
    return return_database_info(moon.self_to_dict())


@moons_bp.route("", methods=["POST"])
def discover_moon():
    request_body = request.get_json()
    new_moon = discover_moon_safely(request_body)

    db.session.add(new_moon)
    db.session.commit()

    return success_message(f"moon {new_moon.name} successfully added to the moons Database.", 201)


@moons_bp.route("/<moon_id>", methods=["PUT", "PATCH"])
def update_moon_by_id(moon_id):
    moon = get_moon_record_by_id(moon_id)

    request_body = request.get_json()
    update_moon_safely(moon, request_body)

    db.session.commit()

    return return_database_info(moon.self_to_dict())


@moons_bp.route("/<moon_id>", methods=["DELETE"])
def delete_moon(moon_id):
    moon = get_moon_record_by_id(moon_id)

    db.session.delete(moon)
    db.session.commit()

    return success_message(f"moon {moon.name} successfully deleted from the moons Database.")

