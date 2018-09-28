from flask import Flask, request, jsonify, session
from . import api2
from .models import Orders, User, Foods
order_class = Orders()
user_class = User()
food_class = Foods()


def validate_user( data):
  """validate user details"""
  try:
      # check if the username is more than 3 characters
      if len(data['username'].strip()) < 3:
          return "username must be more than 3 characters"
      # check if password has space
      elif " " in data["password"]:
          return "password should be one without spaces"
      elif len(data['password'].strip()) < 5:
          return "Password should have atleast 5 characters"
      # check if the passwords match
      elif data['password'] != data['confirmpass']:
          return "passwords do not match"
      else:
          return "valid"
  except Exception as error:
      return "please provide all the fields, missing " + str(error)

def validate_login( data):
  """validate user credentials while loging in"""
  try:
      # check if the username is more than 3 characters
      if len(data['username'].strip()) < 3:
          return "username must be more than 3 characters"
      # check if password has space
      elif " " in data["password"]:
          return "password should be one without spaces"
      elif len(data['password'].strip()) < 5:
          return "Password should have atleast 5 characters"
      else:
          return "valid"
  except Exception as error:
      return "please provide all the fields, missing " + str(error)


@api2.route('/signup', methods=["POST"])
def reg():
  """ Method to create user account."""
  data = request.get_json()
  res = validate_user(data)
  username = data['username']
  password = data['password']
  confirmpass = data['confirmpass']
  addres = data['addres']
  contact = data['contact']
  user_type = data['user_type']
  if res == "valid":
      response = user_class.create(username, password, confirmpass, addres, contact, user_type) 
      return response
  return jsonify({"message":res}), 400


@api2.route('/users', methods=["GET"])
def all_users():
	""" Route to get all the registered users."""
	return user_class.view_users()

@api2.route('/login', methods=["POST"])
def login():
    """ Method to login user """
    data = request.get_json()
    res = validate_login(data)
    username = data['username']
    password = data['password']
    if res == "valid":
      result = user_class.login(username, password)
      return result
    return jsonify({"message":res}), 400

@api2.route('/logout', methods=["GET"])
def logout():
    """ Method to logout user."""
    if 'username' in session:
      session.clear()
      return jsonify({"message":"Logged out"})
    return jsonify({"message":"You are not Logged in"}) 
    

"""
orders
"""
def validate_data(data):
    """validate input data """
    try:
        #check if the food name is provided
        if len(data['food_name']) == 0:
            return "Enter food name"
        # check if food price is valid
        elif "" in data['price']:
            return "Invalid food price"
        #elif data['order_status'] == "accepted" or data['order_status'] != "declined":
            #return "Order status should be accepted or declined"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)

@api2.route('/orders', methods=["GET"])
def all_orders():
	""" Method to place and get Orders."""
	return order_class.all_order(), 200

@api2.route('/orders', methods=['POST'])
def place():
  data = request.get_json()
  res = validate_data(data)
  food_name = data['food_name']
  price = data['price']
  food_id = data['food_id']
  order_status = data['order_status']
  if res == "valid":
    result = order_class.place_order(food_name, price, food_id, order_status)
    return result, 200
  return jsonify({"message":res}), 400


@api2.route('/orders/<int:order_id>', methods=['PUT'])
def update(order_id, **kwargs):
	"""method to return a specific order"""
	result = order_class.update_order(order_id)
	return result, 201

@api2.route('/orders/<int:order_id>', methods=['DELETE'])
def delet(order_id, **kwargs):
  """method to return a specific order"""
  result = order_class.delete_order(order_id)
  return result, 200


"""
food
"""

@api2.route('/food', methods=["GET"])
def all_food():
  """ Method to place and get Orders."""
  return food_class.food_menu()

@api2.route('/food', methods=['POST'])
def add_food():
  data = request.get_json()
  food_name = data['food_name']
  price = data['price']
  quantity = data['quantity']
  return food_class.add_to_menu(food_name, price, quantity)


@api2.route('/food/<int:food_id>', methods=['PUT'])
def update_food(food_id, **kwargs):
  """method to return a specific order"""
  result = food_class.update_menu(food_id)
  return result

@api2.route('/food/<int:food_id>', methods=['DELETE'])
def delete_food(food_id, **kwargs):
  """method to return a specific order"""
  result = food_class.delete_from_menu(food_id)
  return result