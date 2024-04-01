from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_admin

@decorator_autme_admin
async def new_gender():
    try:
        body = request.json
        check_gender = session.query(gender).filter(gender.name == body["name"])
        for i in check_gender:
            return jsonify({"message": "Такой пол уже зарегистрирован"}), 400
        session.add(gender(name=body["name"]))
        session.commit()
        return jsonify({"message": "Новый пол успешно добавлен"}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
