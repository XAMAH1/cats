from datetime import datetime

from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_admin

@decorator_autme_admin
async def new_cats():
    try:
        body = request.json
        n_cats = cats()
        n_cats.name = body["name"]
        result = session.query(breed).filter(breed.name == body["breed"])
        for i in result:
            n_cats.breed = i.id
        result = session.query(color).filter(color.name == body["color"])
        for i in result:
            n_cats.color = i.id
        result = session.query(gender).filter(gender.name == body["gender"])
        for i in result:
            n_cats.gender = i.id
        if n_cats.breed is None or n_cats.color is None or n_cats.gender is None:
            return jsonify({"message": "Проверьте вводимые данные!"}), 400
        try:
            n_cats.age = datetime(int(body["age"].split(" ")[2]), int(body["age"].split(" ")[1]),
                                         int(body["age"].split(" ")[0]))
        except Exception as e:
            print(e)
            return jsonify({"message": f"Не корректный формат даты! Нужный формат '27 10 2023'."}), 400
        if "sings" in body:
            n_cats.sings = body["sings"]
        n_cats.price = body["price"]
        session.add(n_cats)
        session.commit()
        return jsonify({"message": "Новая поизиция успешно добавлена"}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
