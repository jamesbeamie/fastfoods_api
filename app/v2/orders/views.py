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

