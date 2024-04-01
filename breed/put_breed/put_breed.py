from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_admin

@decorator_autme_admin
async def update_breed(breed_id):
    try:
        body = request.json
        check_breed = session.query(breed).filter(breed.id == breed_id)
        for i in check_breed:
            i.name = body["name"]
            session.commit()
            return jsonify({"message": "Изменения успешно внесены"}), 200
        return jsonify({"message": "Такая порода еще не зарегистрированна"}), 400
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
