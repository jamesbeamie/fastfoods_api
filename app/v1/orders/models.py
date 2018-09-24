from flask import jsonify, request
class Orders(object):
    def __init__(self):
        """ Initialize empty order list"""  
        self.all_orders = []        

    def all_order(self):
        """ fetch all orders """
        if len(self.all_orders) > 0:
            return jsonify({"Orders": self.all_orders}), 200
        return jsonify({"message":"Kindly place your order."})

    def return_specific(self, order_id):
        """The function returns a specific order, specified by id"""
        for order in self.all_orders:
            if order['order_id'] == order_id:
                return jsonify({"order":order})

    def place_order(self, food_name, price, food_id, order_status):
        """Create order"""
        self.order = {}
        self.order_id = len(self.all_orders)

        self.order['order_id'] = self.order_id + 1
        self.order['food_name'] = food_name
        self.order['price'] = price
        self.order['food_id'] = food_id
        self.order['order_status'] = order_status

        self.all_orders.append(self.order)
        return jsonify({"message": "Order placed.", "Orders":self.all_orders}), 201

    def update_order(self, order_id):
        """This function edits the order place, takes user inputs in json form"""
        order_details = request.get_json()
        for order_to_update in self.all_orders:
            if order_to_update['order_id'] == order_id:
                order_to_update['food_name'] = order_details['food_name'] 
                order_to_update['price'] = order_details['price']
                order_to_update['food_id'] = order_details['food_id']
                order_to_update['order_status'] = order_details['order_status']
                return jsonify({'Order': self.all_orders})

    # this endpoint deletes the specified(using its id) order from dictionary
    def delete_order(self, order_id):
        """The function deletes an order specified by the id"""
        for order in self.all_orders:
            if order['order_id'] == order_id:
                self.all_orders.remove(order)
                return jsonify({'Orders': self.all_orders, "message":"DELETED"})

class Foods(object):
    def __init__(self):
        """ Initialize empty food list"""  
        self.all_foods = []
        
    def available_food(self):
        """ get all foods """
        if len(self.all_foods) > 0:
            return jsonify({"Foods": self.all_foods}), 200
        return jsonify({"message":"No food available."})
