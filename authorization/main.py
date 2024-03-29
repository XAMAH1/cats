import asyncio

from flask import Blueprint, request
from authorization.login.login_user import login
from authorization.register_user.register_user import register
from authorization.register_user.send_code_mail import check_mail
from authorization.reser_password.reser_user_password import update_password_user
from authorization.reser_password.send_code_reser_passwor import get_code_reset
from reuests_options.requests_options import decorator_options

authorization = Blueprint('authorization', __name__)

@authorization.route("/register", methods=["POST", "OPTIONS"])
def register_new_user():
    return asyncio.run(register())


@authorization.route("/code/register", methods=["POST", "OPTIONS"])
def send_user_code():
    return asyncio.run(check_mail())


@authorization.route("/code/reset", methods=["POST", "OPTIONS"])
def send_user_code_reset():
    return asyncio.run(get_code_reset())


@authorization.route("/reset/password", methods=["PUT", "OPTIONS"])
def reset_user_password():
    return asyncio.run(update_password_user())


@authorization.route("/login", methods=["POST", "OPTIONS"])
def login_user():
    return asyncio.run(login())
