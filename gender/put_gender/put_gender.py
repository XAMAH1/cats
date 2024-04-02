from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_admin

@decorator_autme_admin
async def update_gender(gender_id):
    try:
        body = request.json
        check_gender = session.query(gender).filter(gender.id == gender_id)
        for i in check_gender:
            result = session.query(gender).filter(gender.name == body["name"])
            for j in result:
                return jsonify({"message": "Ошибка! Такой гендер уже зарегистрирован!"}), 400
            i.name = body["name"]
            session.commit()
            return jsonify({"message": "Изменения успешно внесены"}), 200
        return jsonify({"message": "Такой пол не зарегистрирован"}), 400
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
