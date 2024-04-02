import asyncio
from flask import Blueprint, request

from cats.delete_cats.delete_cats import delete_cats
from cats.get_cats.get_cats_all import get_all_cats
from cats.get_cats.get_cats_current import get_cats
from cats.post_cats.new_cats import new_cats
from cats.put_cats.put_cats import update_cats
from reuests_options.requests_options import decorator_options

cats_profile = Blueprint('cats_profile', __name__)


@cats_profile.route("/cats", methods=["POST", "GET"])
@decorator_options
def cats_all():
    if request.method == "POST":
        return asyncio.run(new_cats())
    if request.method == "GET":
        return asyncio.run(get_all_cats())


@cats_profile.route("/cats/<int:cats_id>", methods=["PUT", "GET", "DELETE"])
def current_color(cats_id):
    if request.method == "PUT":
        return asyncio.run(update_cats(cats_id))
    if request.method == "GET":
        return asyncio.run(get_cats(cats_id))
    if request.method == "DELETE":
        return asyncio.run(delete_cats(cats_id))
