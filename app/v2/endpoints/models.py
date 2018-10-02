from flask import jsonify, request, session,make_response
import psycopg2
import jwt
import datetime
from functools import wraps
from  flask_jwt_extended import create_access_token
import os
from ...dbconect import dbcon


class User(object):
    def __init__(self):
        """ Initialize connection to database"""
        #self.con = dbcon()

    def valid_user(self, username):
        """Checks if user exists"""
        con = dbcon()
        cur = con.cursor()
        cur.execute("SELECT * FROM my_users WHERE username=%(username)s", {'username':username})
        rows = cur.rowcount
        if rows > 0:
            
            return True
        return False

    def is_admin(self, username):
        con = dbcon()
        cur = con.cursor()
        cur.execute("SELECT * FROM my_users WHERE username=%(username)s",{"username":username})
        res = cur.fetchone()
        if res[6] != 'admin':
            return False
        return True


    def create(self, username, password, confirmpass, addres, contact, user_type):
        """Create users"""
        if self.valid_user(username):
            return jsonify({"message":"User taken"}),200
        else:
            con = dbcon()
            cur = con.cursor()
            cur.execute("INSERT INTO my_users (username, password, confirmpass, addres, contact, user_type) VALUES (%(username)s,%(password)s,%(confirmpass)s,%(addres)s,%(contact)s,%(user_type)s);",{'username':username,'password':password,'confirmpass':confirmpass,'addres':addres,'contact':contact,'user_type':user_type})
            con.commit()
            return make_response(jsonify({"message":"user created"}), 200)

    def view_users(self):
        con = dbcon()
        cur = con.cursor()
        cur.execute("SELECT * FROM my_users")
        res = cur.fetchall()
        return jsonify({'Users': res}), 200

    def delete_user(self, username):
        con = dbcon()
        cur = con.cursor()
        cur.execute("DELETE FROM my_users WHERE username=%(username)s",{'username':username})
        con.commit()
        return jsonify({'message': 'User deleted'})

    def login(self, username, password):
        if self.valid_user(username):
            con = dbcon()
            cur = con.cursor()
            cur.execute("SELECT * FROM my_users WHERE username=%(username)s and password=%(password)s",{'username':username, 'password':password})
            #rows = cur.rowcount
            user = cur.fetchone()
            if user != None:
                return jsonify({"Your token":create_access_token(username)}), 200
            return jsonify({"message":"User not found"}), 401
        return jsonify({"message":"Please register"})
        
class Foods(object):
    def __init__(self):
        """ Initialize empty order list"""  
        #self.all_orders = []        

    def food_menu(self):
        """ fetch all orders """
        con = dbcon()
        cur = con.cursor()
        cur.execute("SELECT * FROM food;")
        res = cur.fetchall()
        menu_items=[]
        for food in res:
            food_item = {
            'food_id':food[0],
            'food_name':food[1],
            'quantity':food[2],
            'price':food[3]
            }
            menu_items.append(food_item)
        return jsonify({"message":"Food on menu", "Food": menu_items}), 200
