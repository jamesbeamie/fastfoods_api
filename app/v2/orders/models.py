from flask import jsonify, request
import os
import psycopg2
from ...dbconect import dbcon
class Orders(object):
    def __init__(self):
        """ Initialize empty order list"""  
        #self.all_orders = []        

    def all_order(self):
        """ fetch all orders """
        con = dbcon()
        cur = con.cursor()
        cur.execute("SELECT * FROM myorders;")
        res = cur.fetchall()
        return jsonify({"message":"retrieved", "Orders": res}), 200

    def place_order(self, food_name, price, food_id, order_status):
        """Create order"""
        con = dbcon()
        cur = con.cursor()
        cur.execute("INSERT INTO myorders (food_name, price, food_id, order_status) VALUES (%(food_name)s,%(price)s,%(food_id)s,%(order_status)s);",{'food_name':food_name,'price':price,'food_id':food_id,'order_status':order_status})
        con.commit()
        return jsonify({"message":"order created"}), 200

        #self.all_orders.append(self.order)
        #return jsonify({"message": "Order placed.", "Orders":self.all_orders}), 201
