import jwt
from flask import request, jsonify

from config import SECRET_KEY_TOKEN
from database.main import *
from authorization.auth.auth import decorator_autme_user
from get_token.get_token import get_token


@decorator_autme_user
async def get_all_cart():
    try:
        cart_all = []
        token = get_token()
        user_id = jwt.decode(token, SECRET_KEY_TOKEN, algorithms=["HS256"])["user_id"]
        check_cart: cart = session.query(cart).filter(cart.user_id == user_id)
        for current_cart in check_cart:
            check_cats = session.query(cats).filter(cats.id == current_cart.cats_id)
            for i in check_cats:
                cart_all.append({
                    "id": current_cart.id,
                    "cats":
                    {
                        "id": i.id,
                        "name": i.name,
                        "breed": i.breed_realt.name,
                        "color": i.color_realt.name,
                        "gender": i.gender_realt.name,
                        "sings": i.sings,
                        "age": str(i.age),
                        "price": i.price
                    }
                })
        return jsonify({"cart": cart_all}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
