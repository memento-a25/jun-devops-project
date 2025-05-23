import pytest
from ..main import app, REQUEST_COUNT # Import app + counter

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
         yield client

def test_hello_route(client):
    initial_count = REQUEST_COUNT._value.get() # Acquiring current counter value

    response = client.get('/')
    assert response.status_code == 200
    assert "Hello from Flask-app!" in response.data.decode()

    assert REQUEST_COUNT._value.get() == initial_count + 1

def test_metrics_route(client):
    response = client.get('/metrics')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'text/plain; version=0.0.4; charset=utf-8'
