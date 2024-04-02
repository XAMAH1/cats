from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_admin


@decorator_autme_admin
async def delete_cats(cats_id):
    try:
        session.query(cats).filter(cats.id == cats_id).delete()
        return jsonify({"message": "Позиция успешно удалена"}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
