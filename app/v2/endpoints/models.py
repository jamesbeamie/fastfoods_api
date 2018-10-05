
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
        cur.execute("SELECT * FROM my_users WHERE username=%(username)s",\
         {'username':username})
        rows = cur.rowcount
        if rows > 0:
            return True
        return False

    def is_admin(self, username):
        con = dbcon()
        cur = con.cursor()
        cur.execute("SELECT * FROM my_users WHERE username=%(username)s",\
            {"username":username})
        res = cur.fetchone()
        if res[6] != 'admin':
            return False
        return True


    def create(self, username, password, confirmpass, addres, contact, user_type):
        """Create users"""
        if self.valid_user(username):
            return jsonify({"message":"Username already taken"}),201
        else:
            con = dbcon()
            cur = con.cursor()
            cur.execute("INSERT INTO my_users (username, password, confirmpass, \
                addres, contact, user_type) VALUES (%(username)s,%(password)s,\
                %(confirmpass)s,%(addres)s,%(contact)s,%(user_type)s);",\
                {'username':username,'password':password,'confirmpass':confirmpass,\
                'addres':addres,'contact':contact,'user_type':user_type})
            con.commit()
            return make_response(jsonify({"message":"user created successfully"}), 201)

    def view_users(self):
        con = dbcon()
        cur = con.cursor()
        cur.execute("SELECT * FROM my_users")
        res = cur.fetchall()
        user_list=[]
        for user in res:
            user_det = {
            'user_id':user[0],
            'username':user[1],
            'password':user[2],
            'confirmpass':user[3],
            'addres':user[4],
            'contact':user[5],
            'user_type':user[6]
            }
            user_list.append(user_det)
        return jsonify({'Users': user_list}), 200

    def delete_user(self, username):
        con = dbcon()
        cur = con.cursor()
        cur.execute("DELETE FROM my_users WHERE username=%(username)s",\
            {'username':username})
        con.commit()
        return jsonify({'message': 'User deleted successfully'})

    def login(self, username, password):
        if self.valid_user(username):
            con = dbcon()
            cur = con.cursor()
            cur.execute("SELECT * FROM my_users WHERE username=%(username)s \
                and password=%(password)s",{'username':username, 'password':password})
            user = cur.fetchone()
            if user != None:
                return jsonify({"User token":create_access_token(username)}), 200
            return jsonify({"message":"You entered a wrong password"})
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
            'price':food[2]
            }
            menu_items.append(food_item)
        return jsonify({"message":"Food on menu", "Food": menu_items}), 200

    def add_to_menu(self, food_name, price):
        """Create order"""
        con = dbcon()
        cur = con.cursor()
        #if food already exists
        cur.execute("SELECT * FROM food WHERE food_name=%(food_name)s",\
            {"food_name":food_name})
        available = cur.fetchall()
        if available:
            return jsonify({"Message":"Food aready in menu"})
            cur.execute("INSERT INTO food (food_name, price) VALUES (%(food_name)s,\
            %(price)s);",{'food_name':food_name,'price':price})
            con.commit()
            return jsonify({"message":"food added to menu"}), 201

"""
Orders
"""
class Orders(User):
    def __init__(self):
        """ Initialize empty order list""" 

    def all_order_admin(self):
        """ fetch all orders """
        con = dbcon()
        cur = con.cursor()
        cur.execute("SELECT * FROM myorders;")
        res = cur.fetchall()
        my_orders=[]
        for orders in res:
            db_order = {
            'order_id':orders[0],
            'food_name':orders[1],
            'username':orders[2],
            'food_id':orders[3],
            'order_status':orders[4]
            }
            my_orders.append(db_order)
        return jsonify({"Orders": my_orders}), 200

    def all_order_user(self, username):
        """ fetch all orders for a specific user"""
        con = dbcon()
        cur = con.cursor()
        cur.execute("SELECT * FROM myorders;")
        res = cur.fetchall()
        user_orders=[]
        for orders in res:
            user_order = {
            'order_id':orders[0],
            'food_name':orders[1],
            'username':orders[2],
            'food_id':orders[3],
            'order_status':orders[4]
            }
            user_orders.append(user_order)
        return jsonify({"Orders": user_orders}), 200

    def create_order(self, food_name,username,food_id, order_status):
        """Create order"""
        con = dbcon()
        cur = con.cursor()
        #if food already exists
        cur.execute("SELECT * FROM myorders WHERE food_name=%(food_name)s",\
            {"food_name":food_name})
        available = cur.fetchall()
        if available:
            return make_response(jsonify({"Message":"Food already in your orders"}))
        cur.execute("INSERT INTO myorders (food_name,username, food_id, order_status) VALUES (%(food_name)s,%(username)s,%(food_id)s,%(order_status)s);",{'food_name':food_name,'username':username,'food_id':food_id, 'order_status':order_status})
        con.commit()
        return make_response(jsonify({"message":"food added to menu"}),201)

    def update_order(self, order_id):
        """This function edits the order placed, takes user inputs in json form"""
        order_details = request.get_json()
        food_name = order_details['food_name']
        username = order_details['username']
        food_id = order_details['food_id']
        order_status = order_details['order_status']
        
        #if user is admin

        con = dbcon()
        cur = con.cursor()
        cur.execute("UPDATE  myorders SET food_name=%s, username=%s, \
            food_id= %s, order_status= %s WHERE order_id=%s",\
            (food_name, username, food_id, order_status, order_id))
        con.commit()
            
        cur.execute("SELECT * FROM myorders")
        res = cur.fetchall()
        return make_response(jsonify({'message': 'Order updated'}), 201)

    def get_specific_order(self, order_id):
        """The function gets an order specified by the id"""
        con = dbcon()
        cur = con.cursor()
        cur.execute("SELECT * FROM myorders WHERE order_id=%(order_id)s",\
            {'order_id':order_id})
        res = cur.fetchall()
        user_orders=[]
        for orders in res:
            user_order = {
            'order_id':orders[0],
            'food_name':orders[1],
            'username':orders[2],
            'food_id':orders[3],
            'order_status':orders[4]
            }
            user_orders.append(user_order)
        return make_response(jsonify({"order":user_orders}), 200)