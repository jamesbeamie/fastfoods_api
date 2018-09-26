from flask import jsonify, request
import os
import psycopg2
from ...dbconect import dbcon
class Orders(object):
    def __init__(self):
        """ Initialize empty order list"""  
        self.all_orders = []        

    def all_order(self):
        """ fetch all orders """
        con = dbcon()
        cur = con.cursor()
        cur.execute("SELECT * FROM myorders;")
        res = cur.fetchall()
        return jsonify({"message":"retrieved", "Orders": res}), 200

