from flask import request


def get_token():
    token = ""
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split()[1]
    if "Security" in request.headers:
        token = request.headers["Security"].split()[1]
    return token
