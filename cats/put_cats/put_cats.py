from datetime import datetime

from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_admin


@decorator_autme_admin
async def update_cats(cats_id):
    try:
        body = request.json
        check_cats: cats = session.query(cats).filter(cats.id == cats_id)
        for i in check_cats:
            if "name" in body:
                i.name = body["name"]
            if "breed" in body:
                result = session.query(breed).filter(breed.name == body["breed"])
                success = False
                for j in result:
                    i.breed = j.id
                    success = True
                if not success:
                    return jsonify({"message": "Такой породы не существует"}), 400
            if "color" in body:
                result = session.query(color).filter(color.name == body["color"])
                success = False
                for j in result:
                    i.color = j.id
                    success = True
                if not success:
                    return jsonify({"message": "Такого окраса не существует"}), 400
            if "gender" in body:
                result = session.query(gender).filter(gender.name == body["gender"])
                success = False
                for j in result:
                    i.gender = j.id
                    success = True
                if not success:
                    return jsonify({"message": "Такого пола не существует"}), 400
            if "age" in body:
                try:
                    i.age = datetime(int(body["age"].split(" ")[2]), int(body["age"].split(" ")[1]),
                                          int(body["age"].split(" ")[0]))
                except Exception as e:
                    print(e)
                    session.rollback()
                    return jsonify({"message": f"Не корректный формат даты! Нужный формат '27 10 2023'."}), 400
            if "sings" in body:
                i.sings = body["sings"]
            if "price" in body:
                i.price = body["price"]
            session.commit()
            return jsonify({"message": "Изменения успешно внесены"}), 200
        return jsonify({"message": "Такой позиции не существует"}), 400
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
