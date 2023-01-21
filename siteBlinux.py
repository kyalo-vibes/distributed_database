import mysql.connector
import psycopg2

# Site running primary horizontal fragmentation(PHF) on Linux with PostgreSQL. 

# Connecting to the MySQL database on the Windows machine
remote_connection = mysql.connector.connect(
					host = "192.168.100.21",
                    port="3306",
					user = "remote1",
					passwd = "",
					database = "mini_project")

# Preparing a cursor object for the MySQL database
win_cursor = remote_connection.cursor()

# Connecting to the PostgreSQL database on the Linux machine
local_stream = psycopg2.connect(
    host='127.0.0.1',
    port='5432',
    database='mini_project',
    user='postgres',
    password='postgres'
)


def init_fragment():    

    # Preparing a cursor object for the PostgreSQL database
    local_cursor = local_stream.cursor()

    # Create table Products in the PostgreSQL database
    local_cursor.execute("CREATE TABLE IF NOT EXISTS Products (product_id VARCHAR(4) PRIMARY KEY,name VARCHAR(255) NOT NULL,description VARCHAR(255) NOT NULL,price DECIMAL(10, 2) NOT NULL);")
    # Insert data into the Products table, Run this only once
    # local_cursor.execute("INSERT INTO Products (product_id, name, description, price) VALUES ('p001', 'Airforce one', 'A high-quality product that is reliable.', 50.00), ('p002', 'Versace gumboots', 'A durable product that is built to last.', 75.00), ('p003', 'Swiss knife', 'A versatile product that can be used for many purposes.', 100.00), ('p004', 'Bamburi cement', 'A premium product that is made with the best materials.', 150.00), ('p005', 'Shuma ya doshi', 'A unique product that stands out from the rest.', 200.00), ('p006', 'Rolex watch', 'A budget-friendly product that is great value.', 25.00), ('p007', 'Google Pixel 7', 'A cutting-edge product that uses the latest technology.', 200.00), ('p008', 'Gucci handbag', 'A stylish product that looks great.', 125.00), ('p009', 'Fiber wrapping', 'An eco-friendly product that is good for the environment.', 75.00), ('p010', 'power saw', 'A high-performance product that delivers results.', 350.00)")
    local_stream.commit()   # Commit the changes to the database
    
    # Create fragment phf1 where order_date > '2021-01-05' on the PostgreSQL database
    phf1_query = "SELECT * FROM Orders WHERE order_date > '2021-01-05'"
    print("\n ")
    print("Primary Horizontal Fragmentation")
    print("phf1 = SELECT * FROM Orders WHERE order_date > '2021-01-05'")
    local_cursor.execute(phf1_query)
    phf1 = local_cursor.fetchall()
    print(phf1)
    print("")

    # Create fragment phf2 where order_date <= '2021-01-05' on the MySQL database
    win_cursor.execute("DROP TABLE IF EXISTS phf2")
    win_cursor.execute("CREATE TABLE IF NOT EXISTS phf2 (order_id VARCHAR(4) PRIMARY KEY, customer_id INT NOT NULL, order_date DATE NOT NULL, total_amount DECIMAL(10, 2) NOT NULL);")
    print("phf2 = SELECT * FROM Orders WHERE order_date <= '2021-01-05'") 
    local_cursor = local_stream.cursor()
    phf2_query = "SELECT * FROM Orders WHERE order_date <= '2021-01-05'"
    local_cursor.execute(phf2_query)
    phf2 = local_cursor.fetchall()
    print(phf2)
    win_cursor.executemany("INSERT INTO phf2 (order_id, customer_id, order_date, total_amount)VALUES (%s,%s,%s,%s);",phf2)
    # Create view fragment_1 on the MySQL database
    win_cursor.execute("CREATE OR REPLACE VIEW fragment_1 AS SELECT order_id, customer_id, order_date, total_amount FROM phf1;")
    remote_connection.commit()
    print("")


init_fragment()
