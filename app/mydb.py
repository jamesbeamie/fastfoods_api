order_table="""CREATE TABLE IF NOT EXISTS myorders(
						order_id serial PRIMARY KEY,
						food_name VARCHAR(20) NOT NULL,
						price INT NOT NULL,
						food_id INT NOT NULL,
						order_status VARCHAR (30) NOT NULL
					)"""

food_table="""CREATE TABLE IF NOT EXISTS food(
						food_id serial PRIMARY KEY,
						food_name VARCHAR(20) NOT NULL,
						price INT NOT NULL,
						quantity INT NOT NULL
					)"""
user_table="""CREATE TABLE IF NOT EXISTS my_users(
						user_id serial PRIMARY KEY,
						username VARCHAR(20) NOT NULL,
						password VARCHAR(20) NOT NULL,
						confirmpass VARCHAR(20) NOT NULL,
						addres VARCHAR(30) NOT NULL,
						contact INT NOT NULL,
						user_type VARCHAR(10) NOT NULL
					)"""

queries = [order_table, food_table, user_table]