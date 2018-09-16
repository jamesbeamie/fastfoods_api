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

    # Route to return specific order using order id
    @APP.route('/api/v1/orders/<int:order_id>', methods=['GET'])
    def return_specific(order_id):
        """The function returns a specific order, specified by id"""
        order = [order for order in FOOD_ORDERS if order['id'] == order_id ]
        return jsonify({'Order': order})

    # Route to palce an order
    @APP.route('/api/v1/orders', methods=['POST'])
    def place_order():
        """The function takes input data in json form and adds to the food order as new order"""
        order_details = request.get_json()
        placed_order = {
            'id': FOOD_ORDERS[-1]['id'] + 1,
            'name': order_details["name"],
            'Quantity': order_details['Quantity']
        }
        FOOD_ORDERS.append(placed_order)
        return jsonify({'Order': FOOD_ORDERS}), 201

    # Route to update an order
    @APP.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
    def update_order(order_id):
        """This function edits the order place, takes user inputs in json form"""
        order_details = request.get_json()
        updated_order = [order for order in FOOD_ORDERS if order['id'] == order_id]#picking the order
        updated_order[0]['name'] = order_details['name']#editing the name 
        updated_order[0]['Quantity'] = order_details['Quantity']#editing the qty
        return jsonify({'Order': updated_order[0]})

    # this endpoint deletes the specified(using its id) order from dictionary
    @APP.route('/api/v1/orders/<int:order_id>', methods=['DELETE'])
    def delete_order(order_id):
        """The function deletes an order specified by the id"""
        order = [order for order in FOOD_ORDERS if order['id'] == order_id]
        FOOD_ORDERS.remove(order[0])
        return jsonify({'Orders': FOOD_ORDERS})
        
if __name__ == "__main__":
    APP.run(debug=True, port=2500)