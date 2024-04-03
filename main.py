from flask import *

from breed.main import breed_configurator
from cart.main import cart_user
from cats.main import cats_profile
from color.main import color_configurator
from database.main import *
from config import API_HOST, API_PORT
from authorization.main import authorization
from gender.main import gender_configurator
from swagger.main import swaggerui_blueprint
from user.main import user_profile

app = Flask(__name__)


app.register_blueprint(swaggerui_blueprint)
app.register_blueprint(authorization, url_prefix="/api/user")
app.register_blueprint(cats_profile, url_prefix="/api")
app.register_blueprint(cart_user, url_prefix="/api")
app.register_blueprint(breed_configurator, url_prefix="/api")
app.register_blueprint(color_configurator, url_prefix="/api")
app.register_blueprint(gender_configurator, url_prefix="/api")
app.register_blueprint(user_profile, url_prefix="/api/user")


@app.errorhandler(404)
def handle_request_entity_too_large_error(error):
    return {"success": False, "message": "Error path request"}, 404


@app.errorhandler(405)
def handle_request_entity_too_large_error(error):
    return {"success": False, "message": "Error method request"}, 404


@app.errorhandler(500)
def handle_request_entity_too_large_error(error):
    return {"success": False, "message": f"Возникла критическая ошибка сервера. Debug: {error}"}, 500


if __name__ == "__main__":
    app.run(debug=False, host=API_HOST[0], port=API_PORT)
