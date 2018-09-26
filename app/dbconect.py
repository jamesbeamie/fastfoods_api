import psycopg2
import os

import os
import psycopg2

from .mydb import queries

def dbcon():
	#export(should be expoted so that i import)
	#url = os.getenv('DATABASE_URL')

	#set connection
	con = psycopg2.connect('dbname=challenge2 host=localhost user=jimmy password=james23')
	return con

def init_db():
	try:
		connection = dbcon()
		connection.autocommit = True

		#cursor activation
		curs = connection.cursor()
		for query in queries:
			curs.execute(query)
		connection.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print("Database connection error!")
		print(error)



