from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешение CORS для всех маршрутов

data = [{"color": "red", "model": "123"}, {"color": "blue", "model": "133"}]

@app.route('/')
def index():
    return jsonify(data)

@app.route("/getdata", methods = ["post"])
def getdata():
    new_car = request.json
    data.append(new_car)
    print(data)
    return jsonify(data)
if __name__ == "__main__":
    app.run(debug=True)
