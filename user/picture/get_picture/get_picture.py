from authorization.auth.auth import decorator_autme_user
from database.main import *
from flask import request, send_file, jsonify
import jwt
from config import SECRET_KEY_TOKEN
from get_token.get_token import get_token


@decorator_autme_user
async def get_picture_user():
    try:
        token = get_token()
        token = jwt.decode(token, SECRET_KEY_TOKEN, algorithms=["HS256"])
        result = session.query(user).filter(user.login == token["login"])
        for i in result:
            return send_file(i.profile_picture, as_attachment=True), 200
    except Exception as e:
        try:
            session.rollback()
        except:
            pass
        print(e)
        return jsonify({"message": "Ошибка отправки фото!"}), 400
