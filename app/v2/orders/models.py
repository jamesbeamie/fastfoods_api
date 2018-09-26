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

    def update_order(self, order_id):
        """This function edits the order place, takes user inputs in json form"""
        order_details = request.get_json()
        food_name = order_details['food_name'] 
        price = order_details['price']
        food_id = order_details['food_id']
        order_status = order_details['order_status']
        
    
        con = dbcon()
        cur = con.cursor()
        cur.execute("UPDATE  myorders SET food_name=%s, price=%s, food_id= %s, order_status= %s WHERE order_id=%s",(food_name, price, food_id, order_status, order_id))
        con.commit()
            
        cur.execute("SELECT * FROM myorders")
        res = cur.fetchall()
        return jsonify({'Order': res})
