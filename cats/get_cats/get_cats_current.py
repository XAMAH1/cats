from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_user


@decorator_autme_user
async def get_cats(cats_id):
    try:
        check_color = session.query(cats).filter(cats.id == cats_id)
        for i in check_color:
            return jsonify({
                "id": i.id,
                "name": i.name,
                "breed": i.breed_realt.name,
                "color": i.color_realt.name,
                "gender": i.gender_realt.name,
                "sings": i.sings,
                "age": str(i.age),
                "price": i.price
            }), 200
        return jsonify({"message": "Ошибка! Такой позиции не существует"}), 400
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
