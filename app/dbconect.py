import psycopg2
import os

#local imports
from .mydb import queries

def dbcon():
	#export(should be expoted so that i import)
	#url = os.getenv('DATABASE_URL')

	#set connection
	con = psycopg2.connect('dbname=challenge1 host=localhost user=andela password=bootcamp')
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



