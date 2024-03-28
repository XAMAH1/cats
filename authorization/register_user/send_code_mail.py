from database.main import *
from flask import request

from send_mail.main import send_mail


async def check_mail():
    try:
        body = request.json  # mail
        result = session.query(user).filter(user.mail == body['mail'])
        for i in result:
            return {"success": False, "message": "Ошибка! Почта уже занята!"}, 400
        code = send_mail.send_code_register(__name__, body["mail"])
        return {'success': True, "message": "Успешно! Почта свободна", "code": code}, 200
    except Exception as e:
        print(e)
        return {"success": False, "message": e}, 500