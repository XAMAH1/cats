from database.main import *
from flask import request, jsonify

from send_mail.main import send_mail


async def check_mail():
    try:
        body = request.json  # mail
        result = session.query(user).filter(user.mail == body['mail'])
        for i in result:
            return jsonify({"message": "Ошибка! Почта уже занята!"}), 400
        code = send_mail.send_code_register(__name__, body["mail"])
        return jsonify({"message": "Успешно! Почта свободна", "code": code}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": e}), 500