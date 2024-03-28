import datetime

from database.main import *
from flask import request, jsonify
from authorization.md5.string_to_md5 import calculate_md5
import jwt
from config import SECRET_KEY_TOKEN


async def login(is_point=None):
    try:
        body = request.json   # login password device
        hash_password = calculate_md5(body["password"])
        if body["login"] is not None:
            result = session.query(autme).filter(autme.login == body["login"])
            for i in result:
                if i.password == hash_password and not i.isBan:
                    if body["device"] == "РС" or body["device"] == "PC" and i.role == 1:
                        return {"success": False, "message": "Вы не имеете доступа к приложению"}, 400
                    date = datetime.datetime.today()
                    token = jwt.encode({"login": body["login"], "user_id": i.user_realt.id, "date_time": str(date), "isPoint": is_point},
                                       SECRET_KEY_TOKEN, algorithm="HS256")
                    autme_tok = autme_token(login=body["login"], token=token, device=body["device"], type_device=body["type_device"], date=date)
                    session.add(autme_tok)
                    session.commit()
                    return jsonify({"message": "Успешная авторизация", "token": token, "role": i.role}), 200
                if i.isBan:
                    return jsonify({"message": "Ваш аккаунт заблокирован"}), 400
                return jsonify({"message": "Аккаунт с таким паролем не найден"}), 400

        if body["mail"] is not None:
            result = session.query(user).filter(user.mail == body["mail"])
            for i in result:
                if i.autme_realt.password == hash_password and not i.autme_realt.isBan:
                    date = datetime.datetime.today()
                    if body["device"] == "РС" or body["device"] == "PC" and i.role == 1:
                        return {"success": False, "message": "Вы не имеете доступа к приложению"}, 400
                    if i.autme_realt.role_realt.name == "Сотрудник":
                        is_point = 0
                    token = jwt.encode({"login": i.login, "user_id": i.autme_realt.user_realt.id, "date_time": str(date), "isPoint": is_point},
                                       SECRET_KEY_TOKEN, algorithm="HS256")
                    autme_tok = autme_token(login=i.login, token=token, device=body["device"], type_device=body["type_device"], date=date)
                    session.add(autme_tok)
                    session.commit()
                    return jsonify({"message": "Успешная авторизация", "token": token, "role": i.autme_realt.role}), 200
                if i.autme_realt.isBan:
                    return jsonify({"message": "Ваш аккаунт заблокирован"}), 400
                return jsonify({"message": "Аккаунт с таким паролем не найден"}), 400
        return jsonify({"message": "Аккаунт с таким именем пользователя не найден"}), 400
    except Exception as e:
        try:
            session.rollback()
        except:
            pass
        print(e)
        return jsonify({"message": "Не так быстро"}), 400