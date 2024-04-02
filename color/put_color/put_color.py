from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_admin


@decorator_autme_admin
async def update_color(color_id):
    try:
        body = request.json
        check_color = session.query(color).filter(color.id == color_id)
        for i in check_color:
            result = session.query(color).filter(color.name == body["name"])
            for j in result:
                return jsonify({"message": "Ошибка! Такой окрас уже зарегистрирован!"}), 400
            i.name = body["name"]
            session.commit()
            return jsonify({"message": "Изменения успешно внесены"}), 200
        return jsonify({"message": "Такой окраса еще не зарегистрирован"}), 400
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
