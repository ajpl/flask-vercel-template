import os

from flask import (
    Flask,
    jsonify,
    request
)
from werkzeug.exceptions import BadRequest

from .utils import add_up


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or \
    'this-is-super-random-and-crazy'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify({"hello": "this is a flask vercel template"})
    else:
        try:
            name = request.json.get("name")
            status = 200
        except (AttributeError, BadRequest):
            name = "name should be in valid JSON"
            status = 400
        return jsonify({"hello": name}), status


@app.route('/add', methods=['POST'])
def add():
    try:
        x = int(request.json.get("x"))
        y = int(request.json.get("y"))
        value = add_up(x, y)
        status = 200
    except (AttributeError, BadRequest, TypeError, ValueError):
        value = "x and y should be numbers in valid JSON"
        status = 400
    return jsonify({"result": value}), status


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
