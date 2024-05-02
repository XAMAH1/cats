import asyncio
from flask import Blueprint, request
from flask_cors import cross_origin

from reuests_options.requests_options import decorator_options
from user.get_profile.get_profile import get_user_profile
from user.get_profile.get_profile_id import get_user_profile_id
from user.picture.main import user_profile_picture
from user.put_profile.put_profile import put_user_profile

user_profile = Blueprint('user_profile', __name__)
user_profile.register_blueprint(user_profile_picture)


@user_profile.route("/profile", methods=["GET", "PUT", "OPTIONS"])
@cross_origin()
def get_user():
    if request.method == "GET":
        return asyncio.run(get_user_profile())
    if request.method == "PUT":
        return asyncio.run(put_user_profile())


@user_profile.route("/profile/<int:user_id>", methods=["GET", "OPTIONS"])
@cross_origin()
def get_user_id(user_id):
    if request.method == "GET":
        return asyncio.run(get_user_profile_id(user_id))
