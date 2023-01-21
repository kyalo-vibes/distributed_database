# importing required library
import mysql.connector
import psycopg2

#Site running on Windows with mysql. It stores the fragments for Vertical Fragmentation

# connecting to the MySQL database on the Windows machine
dataBase = mysql.connector.connect(
					host = "192.168.100.21",
                    port="3306",
					user = "remote1",
					passwd = "",
					database = "mini_project")

# preparing a cursor object for the MySQL database
cursorObject = dataBase.cursor(buffered=True)

# connecting to the PostgreSQL database on the Linux machine
local_stream = psycopg2.connect(
    host='127.0.0.1',
    port='5432',
    database='mini_project',
    user='postgres',
    password='postgres'
)

# preparing a cursor object for the PostgreSQL database
local_cursor = local_stream.cursor()

# Create fragment Q1 which has affinities A1 and A2(orders.order_date, orders.total_amount)
print("Vertical")
print("Q1 = order_id, order_date, total_amount FROM orders: ")
cursorObject.execute("USE mini_project")
Q1 = "SELECT order_id, order_date, total_amount FROM orders"
cursorObject.execute(Q1)
Q1_result = cursorObject.fetchall()
print(Q1_result)
print("")

# Create fragment Q2 which has affinities A3(customers.name)
print("Q2 = order_id, customers.name FROM orders INNER JOIN customers ON orders.customer_id = customers.customer_id: ")
Q2 = "SELECT order_id, customers.name FROM orders INNER JOIN customers ON orders.customer_id = customers.customer_id"
cursorObject.execute(Q2)
Q2_result = cursorObject.fetchall()
print(Q2_result)
print("")

dataBase.close()
