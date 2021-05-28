from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # ENV
db = SQLAlchemy(app)
CORS(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(150), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    
    def __init__(self, description, completed):
        self.description = description
        self.completed = completed
    

# @app.route('/todo-list', methods=['GET'])
# def todo_list():
#     '''Shows all the tasks'''
    
#     todo_list = []
    
#     return jsonify({'todo_list' : todo_list})


@app.route('/api/add/', methods=['POST'])
def add_task():
    description = request.json['description']
    completed = request.json['completed']
    
    new_task = Task(description, completed)
    
    db.session.add(new_task)
    db.session.commit()
    
    return 'Done'
    

@app.route('/api/tasks/', methods=['GET'])
def get_tasks():
    all_tasks = Task.query.all()
    tasks = []
    
    for task in all_tasks:
        tasks.append({'id' : task.id,
                      'description' : task.description,
                      'completed' : task.completed
                    })
    
    return jsonify({ 'tasks' : tasks })


@app.route('/api/delete/<id>/', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    
    return 'deleted'

@app.route('/api/update/<id>/', methods=['POST'])
def update_task(id):
    if request.method == 'POST':
        task = Task.query.get(id)
        
        description = request.json['description']
        completed = request.json['completed']
        
        task.description = description
        task.completed = completed
        
        db.session.commit()
        
        return 'Done'
    else: 
        return 'error'

@app.route('/api/save/', methods=['GET'])
def save_todolist():
    all_tasks = Task.query.all()
    
    tasks = []
    
    for task in all_tasks:
        tasks.append({'id' : task.id,
                      'description' : task.description,
                      'completed' : task.completed
                    })
    
    with open('todolist.json', 'w') as json_file: # ENV
        json.dump(tasks, json_file)
        
    return 'List saved!'

@app.route('/api/load/', methods=['GET', 'POST'])
def load_todolist():

    # Deleting actual list
    all_tasks = Task.query.all()
    for task in all_tasks:
        db.session.delete(task)
        db.session.commit()

    # Loading ancient list and sending it to frontend
    json_file = open('todolist.json',)  # ENV
    
    data = json.load(json_file)
    
    for task in data: 
        id = task["id"]
        description = task["description"]
        completed = task["completed"]
    
        new_task = Task(description, completed)
        
        db.session.add(new_task)
        db.session.commit()
    
    return 'List loaded'
    

        
        
        
    
    

if __name__ == "__main__":
    app.run(debug=True)