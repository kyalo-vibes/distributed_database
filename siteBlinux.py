import mysql.connector
import psycopg2

remote_connection = mysql.connector.connect(
					host = "192.168.100.21",
                    port="3306",
					user = "remote1",
					passwd = "",
					database = "mini_project")

win_cursor = remote_connection.cursor()

local_stream = psycopg2.connect(
    host='127.0.0.1',
    port='5432',
    database='mini_project',
    user='postgres',
    password='postgres'
)


def init_fragment():    

   
    local_cursor = local_stream.cursor()
    local_cursor.execute("CREATE TABLE IF NOT EXISTS Products (product_id VARCHAR(4) PRIMARY KEY,name VARCHAR(255) NOT NULL,description VARCHAR(255) NOT NULL,price DECIMAL(10, 2) NOT NULL);")
    # local_cursor.execute("INSERT INTO Products (product_id, name, description, price) VALUES ('p001', 'Airforce one', 'A high-quality product that is reliable.', 50.00), ('p002', 'Versace gumboots', 'A durable product that is built to last.', 75.00), ('p003', 'Swiss knife', 'A versatile product that can be used for many purposes.', 100.00), ('p004', 'Bamburi cement', 'A premium product that is made with the best materials.', 150.00), ('p005', 'Shuma ya doshi', 'A unique product that stands out from the rest.', 200.00), ('p006', 'Rolex watch', 'A budget-friendly product that is great value.', 25.00), ('p007', 'Google Pixel 7', 'A cutting-edge product that uses the latest technology.', 200.00), ('p008', 'Gucci handbag', 'A stylish product that looks great.', 125.00), ('p009', 'Fiber wrapping', 'An eco-friendly product that is good for the environment.', 75.00), ('p010', 'power saw', 'A high-performance product that delivers results.', 350.00)")
    local_stream.commit()
    local_data_query = "SELECT * FROM Orders WHERE order_date > '2021-01-05'"

    print("\n ")


    local_cursor.execute(local_data_query)
    local_doctors_query_results = local_cursor.fetchall()
    print(local_doctors_query_results)
    print("")

    win_cursor.execute("DROP TABLE IF EXISTS phf1")
    win_cursor.execute("CREATE TABLE IF NOT EXISTS phf1 (order_id VARCHAR(4) PRIMARY KEY, customer_id INT NOT NULL, order_date DATE NOT NULL, total_amount DECIMAL(10, 2) NOT NULL);")
    local_cursor = local_stream.cursor()
    local_data_query = "SELECT * FROM Orders WHERE order_date <= '2021-01-05'"
    print("\n ")


#   
    local_cursor.execute(local_data_query)
    windows_fragment_results = local_cursor.fetchall()
    print(windows_fragment_results)
    win_cursor.executemany("INSERT INTO phf1 (order_id, customer_id, order_date, total_amount)VALUES (%s,%s,%s,%s);",windows_fragment_results)
    win_cursor.execute("CREATE OR REPLACE VIEW fragment_1 AS SELECT order_id, customer_id, order_date, total_amount FROM phf1;")
    remote_connection.commit()
    print("")


init_fragment()
