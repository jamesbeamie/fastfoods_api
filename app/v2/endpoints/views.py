from flask import Flask, request, jsonify, session
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import api2
from .models import User, Foods
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

@api2.route('users/<string:username>', methods=["DELETE"])
def remove_user(username, **kwargs):
  """Route to delete a user from the db using the user name"""
  res = user_class.delete_user(username)
  return res, 200


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
menu
"""
@api2.route('/menu', methods=["GET"])
def all_food():
  """ Method to available food in the menu."""
  return food_class.food_menu()

@api2.route('/menu', methods=['POST'])
@jwt_required
def add_food():
  logedin = get_jwt_identity()
  adm=user_class.is_admin(logedin)
  if adm == True:
    data = request.get_json()
    food_name = data['food_name']
    price = data['price']
    quantity = data['quantity']
    return food_class.add_to_menu(food_name, price, quantity)

  return jsonify({"message":"unauthorized"}),401