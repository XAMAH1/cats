from flask import *

from config import API_HOST, API_PORT

app = Flask(__name__)


app.run(debug=False, host=API_HOST[0], port=API_PORT)
