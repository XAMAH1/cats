from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_user


@decorator_autme_user
async def get_all_color():
    try:
        color_all = []
        check_color = session.query(color).all()
        for i in check_color:
            color_all.append({"id": i.id, "name": i.name})
        return jsonify({"color": color_all}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
