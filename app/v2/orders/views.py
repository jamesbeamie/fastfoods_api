from flask import Flask, request, jsonify
from . import api2
from .models import Orders
order_class = Orders()

"""
orders
"""
class OrdersViews():
	@api2.route('/orders', methods=["GET"])
	def all_orders():
		""" Method to place and get Orders."""
		return order_class.all_order()
  
	@api2.route('/orders', methods=['POST'])
	def place():
		data = request.get_json()
		food_name = data['food_name']
		price = data['price']
		food_id = data['food_id']
		order_status = data['order_status']
		return order_class.place_order(food_name, price, food_id, order_status)