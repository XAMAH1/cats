import jwt
from flask import request, jsonify

from config import SECRET_KEY_TOKEN
from database.main import *
from authorization.auth.auth import decorator_autme_user
from get_token.get_token import get_token


@decorator_autme_user
async def delete_cart_all():
    try:
        token = get_token()
        user_id = jwt.decode(token, SECRET_KEY_TOKEN, algorithms=["HS256"])["user_id"]
        session.query(cart).filter(cart.user_id == user_id).delete()
        session.commit()
        return jsonify({"message": "Корзина успешно очищена"}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
