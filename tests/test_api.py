import requests
import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject

@pytest.fixture()
def obj_id():
   payload = {
      "name": "Apple MacBook Pro 16",
      "data": {
         "year": 2019,
         "price": 1849.99,
         "CPU model": "Intel Core i9",
         "Hard disk size": "1 TB"
      }
   }
   response = requests.post('https://api.restful-api.dev/objects', json=payload).json()
   yield response['id']
   requests.delete(f'https://api.restful-api.dev/objects/{response['id']}')

def test_create_object():
    new_object_endpoint = CreateObject()
    payload = {
       "name": "Apple MacBook Pro 16",
       "data": {
          "year": 2019,
          "price": 1849.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "1 TB"
       }
    }
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_name(payload['name'])


def test_get_object(obj_id):
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_response_is_200()
    get_obj_endpoint.check_response_id(obj_id)

def test_update_object(obj_id):
    update_obj_endpoint = UpdateObject()
    payload = {
         "name": "Apple MacBook Pro 20",
         "data": {
            "year": 2020,
            "price": 1849.99,
            "CPU model": "M10",
            "Hard disk size": "1 TB"
         }
       }
    update_obj_endpoint.update_by_id(obj_id, payload=payload)
    update_obj_endpoint.check_response_is_200()
    update_obj_endpoint.check_response_name(payload['name'])

def test_delete_object(obj_id):
    delete_obj_endpoint = DeleteObject()
    delete_obj_endpoint.delete_by_id(obj_id)
    delete_obj_endpoint.check_response_is_200()
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_response_is_404()

