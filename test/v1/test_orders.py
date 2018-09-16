"""The module has test for the api"""
import unittest
import json
from app.v1.orders import APP
"""the dictionaries are usd for testing endpoints"""
test_orders={
       'id': 1,
       'name': 'Burger',
       'Quantity': 1
        }
test_update={
       'id': 5,
       'name': 'Burger',
       'Quantity': 1
        }
#class for the unittests
class TestApi(unittest.TestCase):
  """The class with individual tests for individual endpoints"""
  def test_return_all(self):
      """Test if all orders are returned and returns success code,200"""
      result=APP.test_client()
      response =result.get('/api/v1/orders', content_type='application/json')
      self.assertEqual( response.status_code, 200)

  def test_return_specific(self):
    """Test if specified order is returned and returns success code,200"""
    result=APP.test_client()
    #test if the order id is not specified, returns page not found,404
    response =result.get('/api/v1/orders/1', content_type='application/json')
    self.assertEqual( response.status_code, 200)

    response =result.get('/api/v1/orders/', content_type='application/json')
    self.assertEqual( response.status_code, 404)

  def test_place_order(self):
    """Test if new order is placed and returns success code,201"""
    result=APP.test_client()
    response =result.post('/api/v1/orders', data=json.dumps(test_orders), content_type='application/json')
    self.assertEqual( response.status_code, 201)

  def test_update_order(self):
    """Test if an order is updated and returns success code,200"""
    result=APP.test_client()
    response = result.put('/api/v1/orders/5', data=json.dumps(test_update), content_type='application/json')
    self.assertEqual( response.status_code, 200)
if __name__ == "__main__":
	unittest.main()