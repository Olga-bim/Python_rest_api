from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
# con = sqlite3.connect("cars.db")

data=[{"color":"red","model":122},{"color":"blue","model":1242}]

# def add_init_cars():
#     pass
#     cur = con.cursor()
#     cur.execute("CREATE TABLE IF NOT EXIXTS CARS(color, model)")
#     cur.execute(""" INSERT INFO cars ('red'.2024)""")
#     cur.execute(""" INSERT INFO cars ('blue'.2020)""")
#     cur.execute(""" INSERT INFO cars ('yellow'.2021)""")
#     cur.execute(""" INSERT INFO cars ('rwhite'.2023)""")
#     con.commit()

@app.route("/")
def get_data():
    return jsonify(data)


@app.route("/send_data",methods=["post"])
def send_data():
    new_car = request.json
    data.append(new_car)
    print(data)
    return  jsonify(data)


@app.route("/del_data", methods=["POST"])
def del_data():
    # Extract the 'model' of the car to be deleted from the request
    car_to_delete = request.json
   
    # Check if the 'model' key exists in the request
    if "model" not in car_to_delete:
        return jsonify({"status": "error", "message": "No 'model' provided"}), 400
   
    model_to_delete = car_to_delete["model"]
   
    # Filter out the car with the specified 'model'
    global data
    data = [car for car in data if car["model"] != model_to_delete]
   
    return jsonify(data)
if __name__ == "__main__":
    app.run(debug=True)
