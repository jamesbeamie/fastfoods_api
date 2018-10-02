
from flask import jsonify, request
class Orders(object):
    def __init__(self):
        """ Initialize empty order list"""  
        self.all_orders = []        

    def all_order(self):
        """ fetch all orders """
        if len(self.all_orders) > 0:
            return jsonify({"Orders": self.all_orders})
        return jsonify({"message":"Kindly place your order."}), 200

    def return_specific(self, order_id):
        """The function returns a specific order, specified by id"""
        for order in self.all_orders:
            if order['order_id'] == order_id:
                return jsonify({"order":order}), 200

    def place_order(self, food_name, price, food_id, order_status):
        """Create order"""
        self.order = {}
        self.order_id = len(self.all_orders)

        self.order['order_id'] = self.order_id + 1
        self.order['food_name'] = food_name
        self.order['price'] = price
        self.order['food_id'] = food_id
        self.order['order_status'] = order_status
        res = self.all_orders.append(self.order)
        return jsonify({"message": "Order placed."}), 200

    def update_order(self, order_id):
        """This function edits the order place, takes user inputs in json form"""
        order_details = request.get_json()
        for order_to_update in self.all_orders:
            if order_to_update['order_id'] == order_id:
                order_to_update['food_name'] = order_details['food_name'] 
                order_to_update['price'] = order_details['price']
                order_to_update['food_id'] = order_details['food_id']
                order_to_update['order_status'] = order_details['order_status']
                return jsonify({'Order': self.all_orders}),201

    # this endpoint deletes the specified(using its id) order from dictionary
    def delete_order(self, order_id):
        """The function deletes an order specified by the id"""
        for order in self.all_orders:
            if order['order_id'] == order_id:
                self.all_orders.remove(order)
                return jsonify({"message":"DELETED"}), 200

class Foods(object):
    def __init__(self):
        """ Initialize empty list for foods"""  
        self.all_foods = []

    def available_food(self):
        if len(self.all_foods) > 0:
            return jsonify({"Foods": self.all_foods}), 200
        return jsonify({"message":"No food available."})
    def specific_food(self, food_id):
        """The function returns a specific food, specified by id"""
        for a_food in self.all_foods:
            if a_food['food_id'] == food_id:
                return jsonify({"food":a_food}), 200

    def create_food(self, food_name, price, quantity):
        """Create food"""
        self.food = {}
        self.food_id = len(self.all_foods)

        self.food['food_id'] = self.food_id + 1
        self.food['food_name'] = food_name
        self.food['price'] = price
        self.food['quantity'] = quantity
        self.all_foods.append(self.food)
        return jsonify({"message": "Food added.", "Foods":self.all_foods}), 201        

    def update_food(self, food_id):
        """This function edits the order by taking user inputs in json form"""
        food_details = request.get_json()
        for food_to_update in self.all_foods:
            if food_to_update['food_id'] == food_id:
                food_to_update['food_name'] = food_details['food_name'] 
                food_to_update['price'] = food_details['price']
                food_to_update['quantity'] = food_details['quantity']
                return jsonify({'Food': self.all_foods}), 200


    # this endpoint deletes the specified order from dictionary using the order id
    def delete_food(self, food_id):
        """The function deletes an order specified by the id"""
        for food in self.all_foods:
            if food['food_id'] == food_id:
                self.all_foods.remove(food)
                return jsonify({'Foods': self.all_foods, "message":"Food deleted"}), 200

