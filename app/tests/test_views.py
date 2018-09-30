"""The module has test for the api"""
from  flask_jwt_extended import create_access_token 
import unittest
import os
import json
from app import create_app
from app.mydb import queries
"""the dictionaries are used for testing endpoints"""
#class for the unittests

class TestApi(unittest.TestCase):
  user_tok = None
  admin_tok = None
  """The class with individual tests for individual endpoints"""
  def setUp(self):
    """Setting up test client"""
    self.app = create_app(config_name="testing")
    self.client = self.app.test_client

class TestOrder(TestApi):
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
    self.assertEqual( response.status_code, 200)

  def test_update_order(self):
    """Test if an order is updated and returns success code,200"""
    response = self.client().put('/api/v1/orders/5', data=json.dumps(self.test_update), content_type='application/json')
    self.assertEqual( response.status_code, 200)

  def test_delete_order(self):
      """Test if an order is deleted and returns success code,200"""
      response = self.client().delete('/api/v1/orders/1', content_type='application/json')
      self.assertEqual( response.status_code, 200)

      response = self.client().delete('/api/v1/orders/', content_type='application/json')
      self.assertEqual( response.status_code, 404)

class TestFood(TestApi):
  test_food={
       'id': 1,
       'food_name': 'Burger',
       'price': 100,
       'quantity': 100
        }
  def test_all_foods(self):
      """Test if all food returned and returns success code,200"""
      response = self.client().get('/api/v1/food', content_type='application/json')
      self.assertEqual( response.status_code, 200)

  def test_specific_fud(self):
    """Test if specified order is returned and returns success code,200"""
    #test if the order id is not specified, returns page not found,404
    response = self.client().get('/api/v1/food/1', content_type='application/json')
    self.assertEqual( response.status_code, 200)

    response = self.client().get('/api/v1/food/', content_type='application/json')
    self.assertEqual( response.status_code, 404)

  def test_prepared_food(self):
    """Test if new order is placed and returns success code,201"""
    response = self.client().post('/api/v1/food', data=json.dumps(self.test_food), content_type='application/json')
    self.assertEqual( response.status_code, 201)

  def test_update_fud(self):
    """Test if a food is updated and returns success code,200"""
    test_update_fud={
       'food_id': 5,
       'food_name': 'Burger',
       'price': 100,
       'quantity': 100
        }
    response = self.client().put('/api/v1/food/5', data=json.dumps(test_update_fud), content_type='application/json')
    print(response.data)

    self.assertEqual( response.status_code, 200)

  def test_delete_fud(self):
      """Test if an order is deleted and returns success code,200"""
      response = self.client().delete('/api/v1/food/1', content_type='application/json')
      self.assertEqual( response.status_code, 200)

class TestUser(TestApi):
  test_users=[{
        "username": "james",
        "password": "beans",
        "confirmpass":"beans",
        "addres": "Nairobi",
        "contact": 78434,
        "user_type": "admin"
  },
  {
        "username": "ja",
        "password": "b",
        "confirmpass":"beans",
        "addres": "Nairobi",
        "contact": 78434,
        "user_type": "admin"
  },{
        "username": "james",
        "password": "beans"
  },{
        "username": "wafula",
        "password": "james",
        "confirmpass":"james",
        "addres": "Nairobi",
        "contact": 78434,
        "user_type": "user"
  },{
        "username": "wafula",
        "password": "james"
  },]
  test_update={
            "food_id": 1,
            "food_name": "beans",
            "order_id": 1,
            "order_status": "completed",
            "price": 160
        }

  def test_signup_validation_username(self):
      """Test if all orders are returned and returns success code,200"""
      response = self.client().post('/api/v2/signup',
      data=json.dumps(self.test_users[1]), 
        content_type='application/json')
      self.assertEqual( response.status_code, 400)

  def test_signup_validation_password(self):
      """Test if all orders are returned and returns success code,200"""
      response = self.client().post('/api/v2/signup',
      data=json.dumps(self.test_users[1]), 
        content_type='application/json')
      self.assertEqual( response.status_code, 400)

  def test_signup_validation_confirmpass(self):
      """Test if all orders are returned and returns success code,200"""
      response = self.client().post('/api/v2/signup',
      data=json.dumps(self.test_users[1]), 
        content_type='application/json')
      self.assertEqual( response.status_code, 400)

  def test_user_admin_signup(self):
      """Test if all orders are returned and returns success code,200"""
      response = self.client().post('/api/v2/signup',
      data=json.dumps(self.test_users[0]), 
        content_type='application/json')
      self.assertEqual( response.status_code, 200)

  def test_user_signup(self):
      """Test if all orders are returned and returns success code,200"""
      response = self.client().post('/api/v2/signup',
      data=json.dumps(self.test_users[3]), 
        content_type='application/json')
      self.assertEqual( response.status_code, 200)

  def test_admin_signin(self):
      """Test if all orders are returned and returns success code,200"""
      with self.app.app_context():
        response = self.client().post('/api/v2/login',
        data=json.dumps(self.test_users[2]), 
          content_type='application/json')
        admin_tok =create_access_token(self.test_users[2]['username'])
        self.assertEqual( response.status_code, 200)

  def test_user_signin(self):
      """Test if all orders are returned and returns success code,200"""
      with self.app.app_context():
        response = self.client().post('/api/v2/login',
        data=json.dumps(self.test_users[4]), 
          content_type='application/json')
        user_tok =create_access_token(self.test_users[4]['username'])
        self.assertEqual( response.status_code, 200)
    
if __name__ == "__main__":
  unittest.main()