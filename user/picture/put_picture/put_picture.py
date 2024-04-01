from authorization.auth.auth import decorator_autme_user
from database.main import *
from flask import request, jsonify
import jwt
from config import SECRET_KEY_TOKEN, picture_path
import os

from get_token.get_token import get_token

image_formats = ['jpg', 'jpeg', 'png', 'bmp', 'tiff']

@decorator_autme_user
async def put_user_picture():
    try:
        token = get_token()
        token = jwt.decode(token, SECRET_KEY_TOKEN, algorithms=["HS256"])
        photo = request.files['photo']
        if not photo:
            return jsonify({"message": "Выберите фото "}), 400
        if photo.headers["Content-Type"].split("/")[1] not in image_formats:
            return jsonify({"message": "Не поддерживаемый формат фото"}), 400
        try:
            new_path = os.path.join(picture_path, f'{token["login"]}.{photo.headers["Content-Type"].split("/")[1]}')
            result = session.query(user).filter(user.login == token["login"])
            for i in result:
                if os.path.exists(i.profile_picture) and i.profile_picture != r"user/picture/static/picture.png":
                    os.remove(i.profile_picture)
                photo.save(f"{new_path}")
                photo.close()
                i.profile_picture = new_path
            session.commit()
            return jsonify({"message": "Фото успешно изменено"}), 200
        except Exception as e:
            try:
                session.rollback()
            except:
                pass
            return jsonify({"message": 'Некоректный формат фото!'}), 400
    except Exception as e:
        return jsonify({"message": "Выберите фото"}), 400
