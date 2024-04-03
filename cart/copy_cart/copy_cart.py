import jwt
from flask import request, jsonify

from config import SECRET_KEY_TOKEN
from database.main import *
from authorization.auth.auth import decorator_autme_user
from get_token.get_token import get_token


@decorator_autme_user
async def copy_user_cart(user_id):
    try:
        token = get_token()
        login = jwt.decode(token, SECRET_KEY_TOKEN, algorithms=["HS256"])["login"]
        result = session.query(user).filter(user.login == login)
        check_hide_cart_user = session.query(user).filter(user.id == user_id)
        count = 0
        for i in check_hide_cart_user:
            if not i.show_cart:
                return jsonify({"message": "Ошибка! У пользователя закрыта корзина"}), 400
        for user_current in result:
            check_user_cart = session.query(cart).filter(cart.user_id == user_id)
            for j in check_user_cart:
                check_cats_in_user_cart = session.query(cart).filter(cart.user_id == user_current.id, cart.cats_id == j.cats_id)
                if check_cats_in_user_cart.count() == 0:
                    session.add(cart(user_id=user_current.id, cats_id=j.cats_id))
                    count += 1
            session.commit()
            return jsonify({"message": f"Вы успешно скопировали корзину пользователя. В вашу корзину было добавлено {str(count)} новых пизиций"}), 200
        return jsonify({"message": "Ошибка! Пользователь не найден"}), 400
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
