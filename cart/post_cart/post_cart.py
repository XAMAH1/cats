import jwt
from flask import request, jsonify

from config import SECRET_KEY_TOKEN
from database.main import *
from authorization.auth.auth import decorator_autme_user
from get_token.get_token import get_token


@decorator_autme_user
async def new_cat_in_cart():
    try:
        body = request.json
        token = get_token()
        login = jwt.decode(token, SECRET_KEY_TOKEN, algorithms=["HS256"])["login"]
        result = session.query(user).filter(user.login == login)
        for user_current in result:
            check_user_cart = session.query(cart).filter(cart.user_id == user_current.id, cart.cats_id == body["cats_id"])
            for j in check_user_cart:
                return jsonify({"message": "Вы уже добавили данную позицию в корзину"}), 400
            session.add(cart(user_id=user_current.id, cats_id=body["cats_id"]))
            session.commit()
            return jsonify({"message": "Позиция успешно добавлена в корзину"}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
