from datetime import datetime
import logging
from flask import Flask, jsonify, json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/status")
def health():
    data = {"result": "Ok - healthy"}
    logging.debug(f'{datetime.now()} health endpoint was reached')
    return jsonify(data), 200


@app.route("/metrics")
def metric():
    data = {"UserCount": 140, "UserCountActive": 23}
    #other implementation
    response = app.response_class(status=200, response=json.dumps({"data":data, "status":200}), mimetype="Application/JSON")
    logging.debug(f'{datetime.now()} metric endpoint was reached')
    return response
    # return jsonify(data), 200


if __name__ == "__main__":
    logging.basicConfig(filename='error.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
