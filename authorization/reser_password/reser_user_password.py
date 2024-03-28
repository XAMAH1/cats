import jwt
from flask import request

from authorization.md5.string_to_md5 import calculate_md5
from config import SECRET_KEY_TOKEN
from database.main import *
from send_mail.main import send_mail


async def update_password_user():
    body = request.json
    if len(request.json['password']) < 6:
        return {"success": False, "message": "Ошибка! Длина нового пароля не может быть меньше 6 символов"}, 400
    result = session.query(user).filter(user.mail == body["mail"])
    for i in result:
        new_password = calculate_md5(body["password"])
        if i.autme_realt.password == new_password:
            return {"success": False, "message": "Вы уже используете этот пароль"}, 400
        i.autme_realt.password = new_password
        result_autme_token = session.query(autme_token).filter(autme_token.login == i.autme_realt.login)
        for j in result_autme_token:
            session.delete(j)
        session.commit()
        send_mail.send_message(__name__, body["mail"], "Вы успшено изменили пароль!", "Смена пароля")
        return {"success": True, "message": "Пароль успешно изменен"}
    return {"success": False, "message": "Указанной вами почты не найдено"}, 400