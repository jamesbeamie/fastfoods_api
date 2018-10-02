from flask import Flask, request, jsonify
from . import api
from .models import Orders, Foods
order_class = Orders()
food_class = Foods()

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
        elif " " in data['price']:
            return "Invalid food price"
        #elif data['order_status'] == "accepted" or data['order_status'] != "declined":
            #return "Order status should be accepted or declined"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)

class OrdersViews():
	@api.route('/orders', methods=["GET"])
	def all_orders():
	  """ Method to place and get Orders."""
	  available_orders = order_class.all_order()
	  return available_orders

	@api.route('/orders/<int:order_id>', methods=['GET'])
	def specific(order_id, **kwargs):
		"""method to return a specific order"""
		result = order_class.return_specific(order_id)
		if not result:
			return jsonify({"message":"couldn't find order_id"})
		return result, 200


	@api.route('/orders', methods=['POST'])
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
	  return jsonify({"message":res})

	@api.route('/orders/<int:order_id>', methods=['PUT'])
	def update(order_id, **kwargs):
		"""method to return a specific order"""
		result = order_class.update_order(order_id)
		if not result:
			return jsonify({"message":"couldn't find order_id"})
		return result, 201

	@api.route('/orders/<int:order_id>', methods=['DELETE'])
	def to_delete(order_id, **kwargs):
		"""method to return a specific order"""
		result = order_class.delete_order(order_id)
		if not result:
			return jsonify({"message":"couldn't find order_id"})
		return result, 200


"""
food
"""
class FoodViews():
	#route to get all the food available
	@api.route('/food', methods=["GET"])
	def all_foods():
	  """ Method to place and get food."""
	  ready_food = food_class.available_food()
	  return ready_food
	  
	#route to get a specific food
	@api.route('/food/<int:food_id>', methods=['GET'])
	def specific_fud(food_id, **kwargs):
		"""method to return a specific food"""
		result = food_class.specific_food(food_id)
		if not result:
			return jsonify({"message":"couldn't find food_id"})
		return result

	#route to add food the the list of foods
	@api.route('/food', methods=['POST'])
	def prepared_food():
		data = request.get_json()
		food_name = data['food_name']
		price = data['price']
		quantity = data['quantity']
		res = food_class.create_food(food_name, price, quantity)
		return res

	#route to edit food
	@api.route('/food/<int:food_id>', methods=['PUT'])
	def update_fud(food_id, **kwargs):
		"""method to edit details of a specific food"""
		result = food_class.update_food(food_id)
		if not result:
			return jsonify({"message":"couldn't find food_id"})
		return result

	#route to delete food
	@api.route('/food/<int:food_id>', methods=['DELETE'])
	def delete_fud(food_id, **kwargs):
		"""method to clear a specific food"""
		result = food_class.delete_food(food_id)
		if not result:
			return jsonify({"message":"couldn't find food_id"})
		return result