from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_user


@decorator_autme_user
async def get_all_cats():
    try:
        color_all = []
        check_color: cats = session.query(cats).all()
        for i in check_color:
            color_all.append({
                "id": i.id,
                "name": i.name,
                "breed": i.breed_realt.name,
                "color": i.color_realt.name,
                "gender": i.gender_realt.name,
                "sings": i.sings,
                "age": str(i.age),
                "price": i.price
            })
        return jsonify({"cats": color_all}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
