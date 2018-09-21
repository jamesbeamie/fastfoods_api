"""The module has test for the api"""
import unittest
import os
import json
#from flask_testing import TestCase
from app import create_app
"""the dictionaries are used for testing endpoints"""
#class for the unittests

class TestApi(unittest.TestCase):
  """The class with individual tests for individual endpoints"""
  def setUp(self):
    self.app = create_app(config_name="testing")
    self.client = self.app.test_client

class TestOrder(TestApi):
  """creating testing dictionaries"""
  test_orders={
            "food_id": 1,
            "food_name": "beans",
            "order_id": 1,
            "order_status": "completed",
            "price": 160
        }
  test_update={
            "food_id": 1,
            "food_name": "beans",
            "order_id": 1,
            "order_status": "completed",
            "price": 160
        }

  def test_return_all(self):
      """Test if all orders are returned and returns success code,200"""
      response = self.client().get('/api/v1/orders', content_type='application/json')
      self.assertEqual( response.status_code, 200)

  def test_return_specific(self):
    """Test if specified order is returned and returns success code,200"""
    #test if the order id is not specified, returns page not found,404
    response = self.client().get('/api/v1/orders/1', content_type='application/json')
    self.assertEqual( response.status_code, 200)

    response = self.client().get('/api/v1/orders/', content_type='application/json')
    self.assertEqual( response.status_code, 404)

  def test_place_order(self):
    """Test if new order is placed and returns success code,201"""
    response = self.client().post('/api/v1/orders', data=json.dumps(self.test_orders), content_type='application/json')
    self.assertEqual( response.status_code, 201)

  def test_update_order(self):
    """Test if an order is updated and returns success code,200"""
    response = self.client().put('/api/v1/orders/5', data=json.dumps(self.test_update), content_type='application/json')
    self.assertEqual( response.status_code, 200)

  def test_delete_order(self):
      """Test if an order is deleted and returns success code,200"""
      response = self.client().delete('/api/v1/orders/1', content_type='application/json')
      self.assertEqual( response.status_code, 200)
    
if __name__ == "__main__":
  unittest.main()