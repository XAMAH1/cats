import asyncio

from flask import Blueprint, request

from authorization.login.login_user import login
from authorization.register_user.register_user import register
from authorization.register_user.send_code_mail import check_mail
from authorization.reser_password.reser_user_password import update_password_user
from authorization.reser_password.send_code_reser_passwor import get_code_reset
from user.get_profile.get_profile import get_user_profile
from user.picture.delete_picture.delete_picture import delete_picture_user
from user.picture.get_picture.get_picture import get_picture_user
from user.picture.put_picture.put_picture import put_user_picture

user_profile_picture = Blueprint('user_profile_picture', __name__)

@user_profile_picture.route("/picture", methods=["GET", "PUT", "DELETE"])
def user_picture():
    if request.method == "GET":
        return asyncio.run(get_picture_user())
    if request.method == "PUT":
        return asyncio.run(put_user_picture())
    if request.method == "DELETE":
        return asyncio.run(delete_picture_user())
