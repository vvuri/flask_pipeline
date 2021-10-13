import pytest
from flask import Flask
from flask import request

def test_assert():
    a = 4
    assert a==4

def test_get_root():
    pass

def test_about():
    app = Flask(__name__)
    with app.test_request_context('/about', method='GET'):
        assert request.path == '/about'
        assert request.method == 'GET'
