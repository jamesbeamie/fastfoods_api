from flask import jsonify, request, session
import os
import psycopg2
from ...dbconect import dbcon

class User(object):
    def __init__(self):
        """ Initialize connection to database"""
        self.con = dbcon()
    def curs(self):
        """The cursor function"""
        con = dbcon()
        cur = con.cursor()
        return cur


    def valid_user(self, username):
        """Checks if user exists"""
        kasa = self.curs()
        kasa.execute("SELECT * FROM my_users WHERE username=%(username)s", {'username':username})
        rows = kasa.rowcount
        if rows > 0:
            return True
        return False

    def create(self, username, password, confirmpass, addres, contact, user_type):
        """Create users"""
        if self.valid_user(username):
            return jsonify({"mes":"User taken"})
        else:
            kasa = self.curs()
            kasa.execute("INSERT INTO my_users (username, password, confirmpass, addres, contact, user_type) VALUES (%(username)s,%(password)s,%(confirmpass)s,%(addres)s,%(contact)s,%(user_type)s);",{'username':username,'password':password,'confirmpass':confirmpass,'addres':addres,'contact':contact,'user_type':user_type})
            self.con.commit()
            return jsonify({"message":"user created"}), 200

    def view_users(self):
        kasa = self.curs()
        kasa.execute("SELECT * FROM my_users")
        res = kasa.fetchall()
        return jsonify({'Users': res}), 200

    def login(self, username, password):
        if self.valid_user(username):
            kasa = self.curs()
            kasa.execute("SELECT username,addres, contact, user_type FROM my_users WHERE username=%(username)s",{'username':username})
            rows = kasa.rowcount
            if rows >0:
                row = kasa.fetchall()
                for user in row:
                    session['username'] = user[1]
                     
                    session['addres'] = user[3]
                    session['contact'] = user[2]
                    session['user_type'] = user[1]
                return jsonify({"message":"Logged in"}), 200
            return jsonify({"message":"Wrong username"}), 401
        else:
            return jsonify({"message":"You are not registered"}), 401
            

class Orders(User):
    def __init__(self):
        """ Initialize empty order list"""
        self.con = dbcon()  
    def curs(self):
        """The cursor function"""
        con = dbcon()
        cur = con.cursor()
        return cur      

    def all_order(self):
        """ fetch all orders """
        casa = self.curs()
        casa.execute("SELECT * FROM myorders;")
        res = casa.fetchall()
        return jsonify({"message":"retrieved", "Orders": res}), 200

    def place_order(self, food_name, price, food_id, order_status):
        """Create order"""
        casa = self.curs()
        casa.execute("INSERT INTO myorders (food_name, price, food_id, order_status) VALUES (%(food_name)s,%(price)s,%(food_id)s,%(order_status)s);",{'food_name':food_name,'price':price,'food_id':food_id,'order_status':order_status})
        self.con.commit()
        return jsonify({"message":"order created"}), 201

    def update_order(self, order_id):
        """This function edits the order place, takes user inputs in json form"""
        order_details = request.get_json()
        food_name = order_details['food_name'] 
        price = order_details['price']
        food_id = order_details['food_id']
        order_status = order_details['order_status']
        
    
        casa = self.curs()
        casa.execute("UPDATE  myorders SET food_name=%s, price=%s, food_id= %s, order_status= %s WHERE order_id=%s",(food_name, price, food_id, order_status, order_id))
        self.con.commit()
            
        casa.execute("SELECT * FROM myorders")
        res = casa.fetchall()
        return jsonify({'Order': res}), 201

    def delete_order(self, order_id):
        """The function deletes an order specified by the id"""
        casa = self.curs()
        casa.execute("DELETE FROM myorders WHERE order_id=%(order_id)s",{'order_id':order_id})
        self.con.commit()
            
        casa.execute("SELECT * FROM myorders")
        res = casa.fetchall()
        return jsonify({'Order': res}), 200
"""
Food Items
"""
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
        return jsonify({"message":"Food on menu", "Food": res}), 200

    def add_to_menu(self, food_name, price, quantity):
        """Create order"""
        con = dbcon()
        cur = con.cursor()
        cur.execute("INSERT INTO food (food_name, price, quantity) VALUES (%(food_name)s,%(price)s,%(quantity)s);",{'food_name':food_name,'price':price,'quantity':quantity})
        con.commit()
        return jsonify({"message":"food added to menu"}), 201


    def update_menu(self, order_id):
        """This function edits the order place, takes user inputs in json form"""
        order_details = request.get_json()
        food_name = order_details['food_name'] 
        price = order_details['price']
        quantity = order_details['quantity']
    
        con = dbcon()
        cur = con.cursor()
        cur.execute("UPDATE  food SET food_name=%s, price=%s, quantity= %s",(food_name, price,quantity))
        con.commit()
            
        cur.execute("SELECT * FROM food")
        res = cur.fetchall()
        return jsonify({'Food': res}), 201

    # this endpoint deletes the specified(using its id) order from dictionary
    def delete_from_menu(self, food_id):
        """The function deletes an order specified by the id"""
        con = dbcon()
        cur = con.cursor()
        cur.execute("DELETE FROM food WHERE food_id=%(food_id)s",{'food_id':food_id})
        con.commit()
    
        cur.execute("SELECT * FROM food")
        res = cur.fetchall()
        return jsonify({'Food': res}), 200