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

if __name__ == "__main__":
	unittest.main()