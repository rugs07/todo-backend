from flask import Flask,request,jsonify
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app, origins=[
    "http://localhost:5173", 
    "http://localhost:3000", 
    "https://gsaprugwed.netlify.app"
])


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed


@app.route('/tasks', methods=['GET'])
def get_task():
    tasks = Task.query.all()
    return jsonify([
        {'id': task.id, 'title': task.title, 'completed': task.completed}
        for task in tasks
    ])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(title=data.get('title'), completed=False)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id, 'title': new_task.title, 'completed': new_task.completed}), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return '', 204
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    if 'completed' in data:
        task.completed = data['completed']
    if 'title' in data and data['title']:
        task.title = data['title']
    db.session.commit()
    return jsonify({'id': task.id, 'title': task.title, 'completed': task.completed})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=port)

