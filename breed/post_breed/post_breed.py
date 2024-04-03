from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_admin


@decorator_autme_admin
async def new_breed():
    try:
        body = request.json
        check_breed = session.query(breed).filter(breed.name == body["name"])
        for i in check_breed:
            return jsonify({"message": "Такая порода уже зарегистрированна"}), 400
        session.add(breed(name=body["name"]))
        session.commit()
        return jsonify({"message": "Новая порода успешно добавлена"}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
