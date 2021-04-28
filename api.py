from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
CORS(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(150), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    
    def __init__(self, description, completed):
        self.description = description
        self.completed = completed
    
#    def __repr__(self):
#        return self.description


@app.route('/todo-list', methods=['GET'])
def todo_list():
    '''Shows all the tasks'''
    
    todo_list = []
    
    return jsonify({'todo_list' : todo_list})


@app.route('/add', methods=['POST'])
def add_task():
    description = request.json['description']
    completed = request.json['completed']
    
    new_task = Task(description, completed)
    
    db.session.add(new_task)
    db.session.commit()
    
    return 'Done'
    

@app.route('/tasks', methods=['GET'])
def get_tasks():
    all_tasks = Task.query.all()
    tasks = []
    
    for task in all_tasks:
        tasks.append({'id' : task.id,
                      'description' : task.description,
                      'completed' : task.completed
                    })
    
    return jsonify({ 'tasks' : tasks })


@app.route('/delete/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    
    return 'deleted'

@app.route('/update/<id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    
    description = request.json['description']
    completed = request.json['completed']
    
    task.description = description
    task.completed = completed
    
    db.session.commit()
    
    return 'Done'
    

if __name__ == "__main__":
    app.run(debug=True)