from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial sample data
cars = [
    {"id": 1, "name": "Tata Nexon"},
    {"id": 2, "name": "Mahindra XUV700"}
]

# 1. GET Method - To view all cars
@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(cars)

# 2. POST Method - To add a new car
@app.route('/cars', methods=['POST'])
def add_car():
    new_car_data = request.get_json()
    cars.append(new_car_data)
    return jsonify({
        "status": "success",
        "message": "Car added successfully!",
        "all_cars": cars
    }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)