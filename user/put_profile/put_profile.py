import jwt
from flask import request, jsonify

from authorization.auth.auth import decorator_autme_user
from config import SECRET_KEY_TOKEN
from database.main import *
from get_token.get_token import get_token


@decorator_autme_user
async def put_user_profile():
    try:
        body = request.json
        token = get_token()
        token = jwt.decode(token, SECRET_KEY_TOKEN, algorithms=["HS256"])
        result_user = session.query(user).filter(user.login == token["login"])
        for i in result_user:
            if "firstname" in body:
                i.firstname = body["firstname"]
            if "surname" in body:
                i.surname = body["surname"]
            if "patronymicname" in body:
                i.patronymicname = body["patronymicname"]
            if "show_cart" in body:
                try:
                    i.show_cart = body["show_cart"]
                except Exception as e:
                    session.rollback()
                    return jsonify({"message": "Проверьте вводимые данные"}), 400
            session.commit()
            return jsonify({"message": "Данные успешно изменены"}), 200
    except Exception as e:
        try:
            session.rollback()
        except:
            pass
        return jsonify({"message": "Укажите данные"}), 400
