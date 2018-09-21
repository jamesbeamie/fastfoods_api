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