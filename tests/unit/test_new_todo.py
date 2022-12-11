
import pytest
from wa_backend import create_app

def test_new_todo_with_fixture(new_todo): # this is not a functinal test
    """
    GIVEN a Task model 
    WHEN a new todo is created
    THEN check if the description and the completion are defined correctly
    """

    assert new_todo.description == 'Do the dishes'
    assert new_todo.completed == True