from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_admin

@decorator_autme_admin
async def get_all_breed():
    try:
        breed_all = []
        check_breed = session.query(breed).all()
        for i in check_breed:
            breed_all.append({"id": i.id, "name": i.name})
        return jsonify({"breed": breed_all}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
