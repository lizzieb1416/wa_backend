import pytest
from wa_backend import create_app
from wa_backend.apis.tasks import Task_model
from wa_backend.apis.tasks import db

@pytest.fixture(scope='module')
def new_todo():
    todo = Task_model('Do the dishes', True)
    return todo

@pytest.fixture(scope='module')
def flask_app():
    app = create_app()

    client = app.test_client()
    
    yield client

# @pytest.fixture(scope='module')
# def app_with_db(flask_app): 
#     db.create_all()

#     yield flask_app

#     db.session.commit()
#     db.drop_all()

# @pytest.fixture
# def app_with_data(app_with_db):
#     todo = Task_model()
#     todo.description = "Walk the dog"
#     todo.completed = False
#     db.session.add(todo)

#     db.session.commit()

#     yield app_with_db

    


