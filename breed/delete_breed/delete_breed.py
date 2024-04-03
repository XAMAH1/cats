from flask import request, jsonify

from database.main import *
from authorization.auth.auth import decorator_autme_admin


@decorator_autme_admin
async def delete_breed(breed_id):
    try:
        session.query(breed).filter(breed.id == breed_id).delete()
        session.commit()
        return jsonify({"message": "Порода успешно удалена"}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
