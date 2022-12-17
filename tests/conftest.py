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


    


