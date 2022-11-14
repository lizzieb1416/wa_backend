from flask import Blueprint
from flask_restx import Namespace, Resource, fields, Api

import logging
import json

blueprint = Blueprint("tasks_api", __name__, url_prefix="/tasks")

api = Api(blueprint,
          title='Tasks API',
          version='0.0.0',
          description="API to handle tasks requests"
          )


task = api.model('Task', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'description': fields.String(required=True, description='The task details')
})

nm = Namespace("Tasks", description="Todo list tasks management")

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task_model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(150), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, description, completed):
        self.description = description
        self.completed = completed


@nm.route("/")
class TodoList(Resource):
  def get(self):
    all_tasks = Task_model.query.all()
    tasks = []

    for task in all_tasks:
        tasks.append(
            {
                "id": task.id,
                "description": task.description,
                "completed": task.completed,
            }
        )

    return {"tasks": tasks}
    
  # @nm.doc('YOUUPLABOUM')
  @nm.param('description', 'description')
  # @nm.marshal_with(task)
  def post(self, description):
    logging.debug("TASK POST : create a new task")
    logging.debug(f'{description}')

    logging.debug(f'{api}')    
    new_task = Task_model(description, False)
    db.session.add(new_task)
    db.session.commit()
    
    return '200', 200


api.add_namespace(nm, path="/todo")







