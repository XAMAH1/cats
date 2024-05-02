import asyncio
from flask import Blueprint, request
from flask_cors import cross_origin

from breed.delete_breed.delete_breed import delete_breed
from breed.get_breed.get_all_breed import get_all_breed
from breed.get_breed.get_current_breed import get_current_breed
from breed.post_breed.post_breed import new_breed
from breed.put_breed.put_breed import update_breed

breed_configurator = Blueprint('breed_configurator', __name__)


@breed_configurator.route("/breed", methods=["POST", "GET"])
@cross_origin()
def all_breed():
    if request.method == "POST":
        return asyncio.run(new_breed())
    if request.method == "GET":
        return asyncio.run(get_all_breed())


@breed_configurator.route("/breed/<int:breed_id>", methods=["PUT", "GET", "DELETE"])
@cross_origin()
def current_breed(breed_id):
    if request.method == "PUT":
        return asyncio.run(update_breed(breed_id))
    if request.method == "GET":
        return asyncio.run(get_current_breed(breed_id))
    if request.method == "DELETE":
        return asyncio.run(delete_breed(breed_id))
