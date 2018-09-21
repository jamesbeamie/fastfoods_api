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