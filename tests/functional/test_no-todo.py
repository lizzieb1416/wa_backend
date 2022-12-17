import pytest
from wa_backend import create_app


def test_base_route_get(flask_app):
    """
    GIVEN a Flask application configures for testing 
    WhEN the '/' page is request (GET)
    THEN check that the response is valid
    """
    response = flask_app.get('/')
    assert response.status_code == 200
    assert b'youpi' in response.data

def test_base_route_post(flask_app):
    """
    GIVEN a Flask application configures for testing 
    WhEN the '/' page is request (POST)
    THEN check that a '405' status code is returned
    """
    response = flask_app.post('/')
    assert response.status_code == 405
    assert b'youpi' not in response.data

    

