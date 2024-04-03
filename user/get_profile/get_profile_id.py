import jwt
from flask import request, jsonify

from authorization.auth.auth import decorator_autme_user
from database.main import *
from config import SECRET_KEY_TOKEN
from get_token.get_token import get_token


@decorator_autme_user
async def get_user_profile_id(user_id):
    result = session.query(user).filter(user.id == user_id)
    for i in result:
        return {
            "firstname": i.firstname,
            "surname": i.surname,
            "patronymicname": i.patronymicname,
            "show_cart": i.show_cart,
            "create_date": str(i.create_date),
        }, 200
    return jsonify({"message": "Профиль не найден!"}), 400
