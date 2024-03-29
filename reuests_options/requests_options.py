from flask import request, jsonify


def decorator_options(func, *args, **kwargs):
    try:
        def options_request(*args, **kwargs):
            if request.method == 'OPTIONS':
                # Возвращаем правильные заголовки CORS для предварительного запроса
                response = jsonify({'message': 'CORS request allowed'})
                response.headers.add('Access-Control-Allow-Origin', '*')
                response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
                response.headers.add('Access-Control-Allow-Methods', '*')
                return response

            return func(*args, **kwargs)

        return options_request
    except Exception as e:
        return jsonify({"message": "Error"}), 400