from authorization.auth.auth import decorator_autme_user
from database.main import *
from flask import request
import jwt
from config import SECRET_KEY_TOKEN
import os

from get_token.get_token import get_token


@decorator_autme_user
async def delete_picture_user():
    token = get_token()
    token = jwt.decode(token, SECRET_KEY_TOKEN, algorithms=["HS256"])
    try:
        result = session.query(user).filter(user.login == token["login"])
        for i in result:
            if os.path.exists(i.profile_picture) and i.profile_picture != r"user/picture/static/picture.png":
                os.remove(i.profile_picture)
            i.profile_picture = r"user/picture/static/picture.png"
        session.commit()
        return {"success": True, "message": "Фото успешно удалено"}
    except Exception as e:
        try:
            session.rollback()
        except:
            pass
        return 'Некоректный формат фото!', 400