import asyncio
from flask import Blueprint, request

from gender.delete_gender.delete_gender import delete_gender
from gender.get_gender.get_all_gender import get_all_gender
from gender.get_gender.get_current_gender import get_current_gender
from gender.post_gender.post_gender import new_gender
from gender.put_gender.put_gender import update_gender

gender_configurator = Blueprint('gender_configurator', __name__)


@gender_configurator.route("/gender", methods=["POST", "GET"])
def all_color():
    if request.method == "POST":
        return asyncio.run(new_gender())
    if request.method == "GET":
        return asyncio.run(get_all_gender())


@gender_configurator.route("/gender/<int:gender_id>", methods=["PUT", "GET", "DELETE"])
def current_color(gender_id):
    if request.method == "PUT":
        return asyncio.run(update_gender(gender_id))
    if request.method == "GET":
        return asyncio.run(get_current_gender(gender_id))
    if request.method == "DELETE":
        return asyncio.run(delete_gender(gender_id))
