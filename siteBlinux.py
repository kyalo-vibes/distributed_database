import mysql.connector
import psycopg2

# Site running primary horizontal fragmentation(PHF) on Linux with PostgreSQL.
# This is decision site and it performs Reconstruction of the fragments from Derived Horizontal Fragmentation(DHF) on site C

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

def reconstruction():
    local_cursor = local_stream.cursor()
    print("Reconstruction from Derived Horizontal Fragmentation on sqlite: ")
    print("")

    # Create table merged_dhf on the PostgreSQL database
    local_cursor.execute("DROP TABLE IF EXISTS merged_dhf")
    local_cursor.execute("CREATE TABLE IF NOT EXISTS merged_dhf (warehouse_id VARCHAR(5) NOT NULL, product_id VARCHAR(5) NOT NULL, stock_quantity INTEGER NOT NULL, price DECIMAL(10,2) NOT NULL);")

    print("Query one: ")

    # Check all the available tables in the Postgresql database
    print("All tables available in postgresql db: ")
    local_cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    print(local_cursor.fetchall())

    # Reconstruction of Hybrid fragmentation. Schema Integration as we combine fragments from different databases

    # Display dhf3 from the PostgreSQL database
    query1 = "SELECT * FROM dhf3"
    local_cursor.execute(query1)
    query1_update = local_cursor.fetchall()
    print("dhf3 table: (price <= 200) && (stock_quantity > 50)")
    print(query1_update)
    print("")

    #Display dhf4 from the PostgreSQL database
    query2 = "SELECT * FROM dhf4"
    local_cursor.execute(query2)
    query2_update = local_cursor.fetchall()
    print("dhf4 table: (price <= 200) && (stock_quantity <= 50)")
    print(query2_update)
    print("")

    # #Doing reconstrcution of dhf3 and dhf4
    #Using UNION statement to perform reconstruction
    merge_query1 = "SELECT * FROM dhf3 UNION SELECT * FROM dhf4"
    local_cursor.execute(merge_query1)
    merge_update1 = local_cursor.fetchall()
    local_cursor.executemany("INSERT INTO merged_dhf (warehouse_id, product_id, stock_quantity, price)VALUES (%s,%s,%s,%s);",merge_update1)
    local_stream.commit()
    print("Merged table: ) ")
    print(merge_update1)
    print("")

     # Display dhf1 table from the MySQL database
    query3 = "SELECT * FROM dhf1"
    win_cursor.execute(query1)
    query3_update = win_cursor.fetchall()
    print("dhf1 table: (price <= 200) && (stock_quantity > 50)")
    print(query3_update)
    print("")

    #Display dhf2 table from the MySQL database
    query4 = "SELECT * FROM dhf2"
    win_cursor.execute(query4)
    query4_update = win_cursor.fetchall()
    print("dhf2 table: (price <= 200) && (stock_quantity <= 50")
    print(query4_update)
    print("")

    # Doing reconstrcution of dhf3 and dhf4
    # Using UNION statement to perform reconstruction
    merge_query2 = "SELECT * FROM dhf1 UNION SELECT * FROM dhf2"
    win_cursor.execute(merge_query2)
    merge_update2 = win_cursor.fetchall()
    local_cursor.executemany("INSERT INTO merged_dhf (warehouse_id, product_id, stock_quantity, price)VALUES (%s,%s,%s,%s);",merge_update2)
    local_stream.commit()
    print("Merged table: dhf1 && dhf2) ")
    print(merge_update2)
    print("")

    # Display result of reconstruction
    merge_result = "SELECT * FROM merged_dhf"
    local_cursor.execute(merge_result)
    final_merge = local_cursor.fetchall()
    print("Reconstructed table: dhf1 && dhf2 && dhf3 && dhf4) ")
    print(final_merge)
    print("")


reconstruction()