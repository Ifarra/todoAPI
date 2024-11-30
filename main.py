import os
from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)
API_URL = "http://localhost:8000/todo"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todos', methods=['GET'])
def get_all_todos():
    response = requests.get(API_URL)
    return jsonify(response.json()), response.status_code

@app.route('/todos/<int:id>', methods=['GET'])
def get_todo_by_id(id):
    response = requests.get(f"{API_URL}/{id}")
    return jsonify(response.json()), response.status_code

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    response = requests.post(API_URL, json=data)
    return jsonify(response.json()), response.status_code

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.json
    response = requests.put(f"{API_URL}/{id}", json=data)
    return jsonify(response.json()), response.status_code

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    response = requests.delete(f"{API_URL}/{id}")
    return jsonify(response.json()), response.status_code

@app.route('/todos/<int:id>/finish', methods=['PATCH'])
def finish_todo(id):
    response = requests.patch(f"{API_URL}/{id}/finish")
    return jsonify(response.json()), response.status_code

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
