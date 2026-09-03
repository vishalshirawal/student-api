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


@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    for student in student_data:
        if student['id'] == student_id:
            return jsonify(student)

    return jsonify({'message': 'Student not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)