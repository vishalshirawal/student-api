from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the Flask API!'})


@app.route('/hello', methods=['POST'])
def hello():
    return jsonify({'message': 'Hello, World!'})

student_data = [
    {'id': 1, 'name': 'John Doe', 'age': 20},
    {'id': 2, 'name': 'Jane Smith', 'age': 22},
    {'id': 3, 'name': 'Alice Johnson', 'age': 19}   
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(student_data)




if __name__ == '__main__':
    app.run(debug=True)