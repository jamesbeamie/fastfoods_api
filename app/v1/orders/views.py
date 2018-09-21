from flask import Flask, request, jsonify
from . import api
from .models import Orders

order_class = Orders()
"""
orders
"""
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
		return result

	@api.route('/orders', methods=['POST'])
	def place():
		data = request.get_json()
		name = data['name']
		price = data['price']
		res = order_class.place_order(name, price)
		return res

	@api.route('/orders/<int:order_id>', methods=['PUT'])
	def update(order_id, **kwargs):
		"""method to return a specific order"""
		result = order_class.update_order(order_id)
		if not result:
			return jsonify({"message":"couldn't find order_id"})
		return result

	@api.route('/orders/<int:order_id>', methods=['DELETE'])
	def to_delete(order_id, **kwargs):
		"""method to return a specific order"""
		result = order_class.delete_order(order_id)
		if not result:
			return jsonify({"message":"couldn't find order_id"})
		return result
