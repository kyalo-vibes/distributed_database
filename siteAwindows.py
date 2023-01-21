# importing required library
import mysql.connector
import psycopg2

#Site running on Windows with mysql. It stores the fragments for Derived Horizontal Fragmentation and Vertical Fragmentation

# connecting to the database
dataBase = mysql.connector.connect(
					host = "192.168.100.21",
                    port="3306",
					user = "remote1",
					passwd = "",
					database = "mini_project")

# preparing a cursor object
cursorObject = dataBase.cursor(buffered=True)


local_stream = psycopg2.connect(
    host='127.0.0.1',
    port='5432',
    database='mini_project',
    user='postgres',
    password='postgres'
)

local_cursor = local_stream.cursor()

print("Vertical")
print("Q1 = order_id, order_date, total_amount FROM orders: ")
cursorObject.execute("USE mini_project")
query4 = "SELECT order_id, order_date, total_amount FROM orders"
cursorObject.execute(query4)
query_four_result = cursorObject.fetchall()
print(query_four_result)
print("")

print("Q2 = order_id, customers.name FROM orders INNER JOIN customers ON orders.customer_id = customers.customer_id: ")
query5 = "SELECT order_id, customers.name FROM orders INNER JOIN customers ON orders.customer_id = customers.customer_id"
cursorObject.execute(query5)
query_five_result = cursorObject.fetchall()
print(query_five_result)
print("")

dataBase.close()
