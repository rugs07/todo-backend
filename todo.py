from flask import Flask,request,jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])


tasks = []

@app.route('/tasks',methods=['GET'])
def get_task():
    return jsonify(tasks)
    
@app.route('/tasks',methods=['POST'])
def add_task():
    data = request.get_json()
    task = {
        'id': len(tasks) +1,
        'title': data.get('title'),
        'completed': False
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
        global tasks
        tasks = [task for task in tasks if task['id'] != task_id]
        return '',204

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            # Toggle completion if requested
            if 'completed' in data:
                task['completed'] = data['completed']
            else:
                task['completed'] = not task['completed']
            # Update title if provided
            if 'title' in data and data['title']:
                task['title'] = data['title']
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

