from database.main import *
from flask import request, jsonify


def decorator_autme_user(func, *args, **kwargs):
    try:
        async def test_autme_user(*args, **kwargs):
            resp = auth()
            if not resp["success"]:
                return jsonify({"message": resp["message"]}), 401
            return await func(*args, **kwargs)

        return test_autme_user
    except Exception as e:
        return jsonify({"message": "Укажите токен"}), 401

def decorator_autme_admin(func, *args, **kwargs):
    try:
        async def test_autme_user(*args, **kwargs):
            resp = auth_admin()
            if not resp["success"]:
                return jsonify({"message": resp["message"]}), 401
            return await func(*args, **kwargs)

        return test_autme_user
    except Exception as e:
        return jsonify({"message": "Укажите токен"}), 401


def auth():
    try:
        token = ""
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split()[1]
        if "Security" in request.headers:
            token = request.headers["Security"].split()[1]
        result = session.query(autme_token).filter(autme_token.token == token)
        for i in result:
            return {"success": True}
        return {"success": False,
                "message": "Ваш токен для авторизации не действителен"}
    except Exception as e:
        try:
            session.rollback()
        except:
            pass
        return {"success": False,
                "message": "Ваш токен для авторизации не действителен"}


def auth_admin():
    try:
        token = ""
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split()[1]
        if "Security" in request.headers:
            token = request.headers["Security"].split()[1]
        result = session.query(autme_token).filter(autme_token.token == token)
        for i in result:
            if i.autme_realt.role == 2:
                return {"success": True}
            return {"success": False,
                    "message": "Ваш токен для авторизации не действителен или вы не являетесь администратором"}
        return {"success": False,
                "message": "Ваш токен для авторизации не действителен или вы не являетесь администратором"}
    except Exception as e:
        try:
            session.rollback()
        except:
            pass
        return {"success": False, "message": "Укажите токен авторизации"}