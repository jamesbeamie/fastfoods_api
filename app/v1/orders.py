"""An api with end points for the orders page of the fast-food-fast application"""
from flask import Flask, jsonify, request
APP = Flask(__name__)
"""The API use data from data structures, dictionaries"""
FOOD_ORDERS = [
    {
        'id': 1,
        'name': 'Pizza',
        'Quantity': 2
    },
    {
        'id': 2,
        'name': 'Chicken curry',
        'Quantity': 4
    },
    {
        'id': 3,
        'name': 'Burger',
        'Quantity': 1
    },
    {
        'id': 4,
        'name': 'Chicken bite',
        'Quantity': 3
    }
]

class Orders(object):
    """constructor"""
    def __init__(self):
        #initializing the counter
        self.order_id_counter = 0

    # Route to return all orders

    @APP.route('/api/v1/orders', methods=['GET'])
    def return_all():
        """The function returns a jsonified list of dictionaries of orders """
        return jsonify({'Orders': FOOD_ORDERS})
if __name__ == "__main__":
    APP.run(debug=True, port=2500)