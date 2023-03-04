from fastapi.testclient import TestClient
from app import app


def test_create():

   client = TestClient(app)

   todo = {
      'name': '04/03/2023',
      'email': '08:32',
      'password': '57°'
   }

   response = client.post(
      '/',
      json=todo
   )

   assert response.status_code == 200, response.text
   data = response.json()
   assert data['name'] == todo['name']


def test_get_all():

   client = TestClient(app)

   response = client.get('/users')

   assert response.status_code == 200, response.text
