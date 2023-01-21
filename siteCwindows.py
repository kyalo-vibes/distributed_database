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
# local_cursor.execute("USE mini_project")
print("Derived Horizontal") 
print("")
# Step 1: Perform PHF on the Products table
 #Query to create fragment LOC1 WHERE [price > 200] ";
cursorObject.execute("DROP TABLE IF EXISTS loc1")
cursorObject.execute("CREATE TABLE IF NOT EXISTS loc1 (SELECT * FROM products WHERE price > 200)")
cursorObject.execute("SELECT * FROM loc1")
loc1_result = cursorObject.fetchall()
print("LOC1: price > 200' ")
print(loc1_result)
print("")

cursorObject.execute("DROP TABLE IF EXISTS dhf1")
cursorObject.execute("CREATE TABLE IF NOT EXISTS dhf1 (SELECT inventory.warehouse_id, loc1.product_id, inventory.stock_quantity, loc1.price FROM inventory INNER JOIN loc1 ON loc1.product_id = inventory.product_id WHERE inventory.stock_quantity > 50);")
cursorObject.execute("SELECT * FROM dhf1")
query_two_result = cursorObject.fetchall()
print("dhf1: inventory x loc1 ")
print(query_two_result)
print("")
#End

cursorObject.execute("DROP TABLE IF EXISTS dhf2")
cursorObject.execute("CREATE TABLE IF NOT EXISTS dhf2 (SELECT inventory.warehouse_id, loc1.product_id, inventory.stock_quantity, loc1.price FROM inventory INNER JOIN loc1 ON loc1.product_id = inventory.product_id WHERE inventory.stock_quantity <= 50)")
cursorObject.execute("SELECT * FROM dhf2")
query_three_result = cursorObject.fetchall()
print("dhf2: inventory x loc1 ")
print(query_three_result)
print("")
#End


local_cursor.execute("DROP TABLE IF EXISTS loc2")
local_cursor.execute("CREATE TABLE IF NOT EXISTS loc2 AS SELECT * FROM products WHERE price <= 200;")
local_cursor.execute("SELECT * FROM loc2")
loc2_result = local_cursor.fetchall()
print("LOC2: price <= 200 ")
print(loc2_result)
print("")


local_cursor.execute("DROP TABLE IF EXISTS dhf3")
local_cursor.execute("CREATE TABLE IF NOT EXISTS dhf3 AS (SELECT inventory.warehouse_id, loc2.product_id, inventory.stock_quantity, loc2.price FROM inventory INNER JOIN loc2 ON loc2.product_id = inventory.product_id WHERE inventory.stock_quantity > 50);")
local_cursor.execute("SELECT * FROM dhf3")
query_three_result = local_cursor.fetchall()
print("dhf3: inventory x loc2 ")
print(query_three_result)
print("")
#End


local_cursor.execute("DROP TABLE IF EXISTS dhf4")
local_cursor.execute("CREATE TABLE IF NOT EXISTS dhf4 AS (SELECT inventory.warehouse_id, loc2.product_id, inventory.stock_quantity, loc2.price FROM inventory INNER JOIN loc2 ON loc2.product_id = inventory.product_id WHERE inventory.stock_quantity <= 50)")
local_cursor.execute("SELECT * FROM dhf4")
query_three_result = local_cursor.fetchall()
print("dhf4: inventory x loc2 ")
print(query_three_result)
print("")
#End
local_stream.commit()
# disconnecting from server
dataBase.close()
