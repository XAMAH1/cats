import asyncio

from flask import Blueprint, request

from authorization.register_user.register_user import register
from authorization.register_user.send_code_mail import check_mail
from authorization.reser_password.reser_user_password import update_password_user
from authorization.reser_password.send_code_reser_passwor import get_code_reset

authorization = Blueprint('authorization', __name__)

@authorization.post("/register")
def register_new_user():
    return asyncio.run(register())


@authorization.post("/code/register")
def send_user_code():
    return asyncio.run(check_mail())


@authorization.post("/code/reset")
def send_user_code_reset():
    return asyncio.run(get_code_reset())


@authorization.put("/reset/password")
def reset_user_password():
    return asyncio.run(update_password_user())

@authorization.errorhandler(500)
def handle_request_entity_too_large_error(error):
    return {"success": False, "message": f"Возникла критическая ошибка сервера. Debug: {error}"}, 400