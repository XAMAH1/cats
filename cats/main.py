import asyncio
from flask import Blueprint, request

from reuests_options.requests_options import decorator_options
from user.get_profile.get_profile import get_user_profile
from user.picture.main import user_profile_picture
from user.put_profile.put_profile import put_user_profile

cats_profile = Blueprint('cats_profile', __name__)


@cats_profile.route("/new", methods=["POST"])
@decorator_options
def get_user():
    if request.method == "POST":
        return asyncio.run(get_user_profile())
