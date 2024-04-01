import asyncio
from flask import Blueprint, request

from color.delete_color.delete_color import delete_color
from color.get_color.get_all_color import get_all_color
from color.get_color.get_current_color import get_current_color
from color.post_color.post_color import new_color
from color.put_color.put_color import update_color

color_configurator = Blueprint('color_configurator', __name__)


@color_configurator.route("/color", methods=["POST", "GET"])
def all_color():
    if request.method == "POST":
        return asyncio.run(new_color())
    if request.method == "GET":
        return asyncio.run(get_all_color())


@color_configurator.route("/color/<int:color_id>", methods=["PUT", "GET", "DELETE"])
def current_color(color_id):
    if request.method == "PUT":
        return asyncio.run(update_color(color_id))
    if request.method == "GET":
        return asyncio.run(get_current_color(color_id))
    if request.method == "DELETE":
        return asyncio.run(delete_color(color_id))
