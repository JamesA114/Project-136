from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)
#create a route
@app.route("/")
def display():
    return jsonify({
        "total_data":data,
        "message": "Successfully executed",
    }), 200

@app.route("/planet")
def planet_data():
    n = request.args.get("name")
    d = next(i for i in data if i['name'] == n)
    return jsonify({
        "planet_data":d,
        "message": "Successfully executed",
    }), 200

#execute the api
if __name__ == "__main__":
    app.run()