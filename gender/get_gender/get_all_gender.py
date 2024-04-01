from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_user


@decorator_autme_user
async def get_all_gender():
    try:
        gender_all = []
        check_gender = session.query(gender).all()
        for i in check_gender:
            gender_all.append({"id": i.id, "name": i.name})
        return jsonify({"gender": gender_all}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
