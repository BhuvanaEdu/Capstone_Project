import pytest
from app import app  # Replace 'your_flask_app_module' with the actual module name

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login(client):
    response = client.get('/login')
    assert response.status_code == 200

def test_register(client):
    response = client.get('/register')
    assert response.status_code == 200

# def test_submit_estimation(client):
#     response = client.get('/submit_estimation')
#     assert response.status_code == 201

# def test_submit_estimation(client):
#     response = client.get('/submit_estimation')
#     assert response.status_code == 302  
#     assert response.location == 'URL_of_the_redirected_page' 

def test_update_estimation_data_collection(client):
    response = client.get('/register')
    assert response.status_code == 201
