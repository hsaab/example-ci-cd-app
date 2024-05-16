import pytest
from server import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_template(client):
    response = client.get('/')
    assert b"This is Massively" in response.data
