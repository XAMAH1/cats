import datetime

from database.main import *
from flask import request
from authorization.md5.string_to_md5 import calculate_md5


async def register():
    try:
        body = request.json
        if "@" in body["login"][1:]:
            return {"success": False, "message": "Ошибка! В логин может содержать @ только на 1 месте"}, 400
        result = session.query(user).filter(user.login == body["login"])
        if result.count() != 0:
            return {"success": False, "message": "Ошибка! Логин уже занят!"}, 400
        result = session.query(user).filter(user.mail == body["mail"])
        if result.count() != 0:
            return {"success": False, "message": "Ошибка! Почта уже занята!"}, 400
        if "patronymicname" not in body:
            body["patronymicname"] = ""
        hash_password = calculate_md5(body["password"])
        try:
            age_date = datetime.datetime(int(body["age"].split(" ")[2]), int(body["age"].split(" ")[1]), int(body["age"].split(" ")[0]))
        except Exception as e:
            print(e)
            return {"success": False, "message": f"Не корректный формат даты! Нужный формат '27 10 2023'."}, 400
        new_user = user(
            login=body["login"],
            mail=body["mail"],
            age=age_date,
            firstname=body["firstname"],
            surname=body["surname"],
            patronymicname=body["patronymicname"],
            profile_picture=r"picture/static/picture.png",
            create_date=datetime.datetime.today()
        )
        session.add(new_user)

        new_autme = autme(login=body["login"], password=hash_password, role=1)
        session.add(new_autme)
        try:
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
            return {"success": False, "message": "К сожалению логин уже занят"}, 400
        return {"success": True, "message": "Аккаунт успешно зарегестрирован"}
    except Exception as e:
        print(e)
        return {"success": False, "message": "Ошибка!"}, 400
