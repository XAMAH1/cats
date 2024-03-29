import asyncio

from flask import Blueprint, request, jsonify

from authorization.login.login_user import login
from authorization.register_user.register_user import register
from authorization.register_user.send_code_mail import check_mail
from authorization.reser_password.reser_user_password import update_password_user
from authorization.reser_password.send_code_reser_passwor import get_code_reset
from reuests_options.requests_options import decorator_options
from user.get_profile.get_profile import get_user_profile
from user.picture.main import user_profile_picture
from user.put_profile.put_profile import put_user_profile

user_profile = Blueprint('user_profile', __name__)
user_profile.register_blueprint(user_profile_picture)


@user_profile.route("/profile", methods=["GET", "PUT", "OPTIONS"])
@decorator_options
def get_user():
    if request.method == "GET":
        return asyncio.run(get_user_profile())
    if request.method == "PUT":
        return asyncio.run(put_user_profile())
