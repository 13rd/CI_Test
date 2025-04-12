import pytest
from web.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'

def test_true():
    assert 1 == 1