import jwt
from flask import request, jsonify

from config import SECRET_KEY_TOKEN
from database.main import *
from send_mail.main import send_mail


async def get_code_reset():
    body = request.json
    result = session.query(user).filter(user.mail == body['mail'])
    if result.count() == 0:
        return jsonify({"message": "Ошибка! Почты не существует!"}), 400
    code = send_mail.send_code(__name__, body["mail"], "востановление пароля")
    return jsonify({"message": "Успешно!", "code": code}), 200
