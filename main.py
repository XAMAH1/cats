from flask import *

from database.main import *
from config import API_HOST, API_PORT
from authorization.main import authorization
from swagger.main import swaggerui_blueprint

app = Flask(__name__)


app.register_blueprint(swaggerui_blueprint)
app.register_blueprint(authorization, url_prefix="/api/user")


@app.errorhandler(404)
def handle_request_entity_too_large_error(error):
    return {"success": False, "message": "Error path request"}, 404


@app.errorhandler(405)
def handle_request_entity_too_large_error(error):
    return {"success": False, "message": "Error method request"}, 404


if __name__ == "__main__":
    app.run(debug=False, host=API_HOST[0], port=API_PORT)
