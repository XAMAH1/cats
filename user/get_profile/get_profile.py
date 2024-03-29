import jwt
from flask import request, jsonify

from authorization.auth.auth import decorator_autme_user
from database.main import *
from config import SECRET_KEY_TOKEN


@decorator_autme_user
async def get_user_profile():
    login = jwt.decode(request.headers["Authorization"].split()[1], SECRET_KEY_TOKEN, algorithms=["HS256"])["login"]
    result = session.query(user).filter(user.login == login)
    for i in result:
        return {
            "firstname": i.firstname,
            "surname": i.surname,
            "patronymicname": i.patronymicname,
            "age": str(i.age),
            "mail": i.mail,
            "show_cart": i.show_cart,
            "create_date": str(i.create_date),
        }
    return jsonify({"message": "Ваш аккаунт не найден, авторизуйтесь снова"}), 401
