from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_admin


@decorator_autme_admin
async def delete_color(color_id):
    try:
        session.query(color).filter(color.id == color_id).delete()
        session.commit()
        return jsonify({"message": "Окрас успешно удален"}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
