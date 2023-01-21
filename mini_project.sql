-- CREATE DATABASE mini_project;
DROP TABLE mini_project.customers;
CREATE TABLE customers (customer_id INT, name VARCHAR(255), address VARCHAR(255), phone VARCHAR(255), email VARCHAR(255));

insert into customers (customer_id, name, address, phone, email) values (1, 'John Smith', 'Nairobi', '555-555-5555', 'johnsmith@email.com');
insert into customers (customer_id, name, address, phone, email) values (2, 'Jane Doe', 'Nakuru', '555-555-5556', 'janedoe@email.com');
insert into customers (customer_id, name, address, phone, email) values (3, 'Michael Johnson', 'Nairobi', '555-555-5557', 'michaeljohnson@email.com');
insert into customers (customer_id, name, address, phone, email) values (4, 'Susan Garcia', 'Mombasa', '555-555-5558', 'susangarcia@email.com');
insert into customers (customer_id, name, address, phone, email) values (5, 'Robert Martinez', 'Nakuru', '555-555-5559', 'robertmartinez@email.com');
insert into customers (customer_id, name, address, phone, email) values (6, 'Laura Davis', 'Nairobi', '555-555-5560', 'lauradavis@email.com');
insert into customers (customer_id, name, address, phone, email) values (7, 'Thomas Wilson', 'Nairobi', '555-555-5561', 'thomaswilson@email.com');
insert into customers (customer_id, name, address, phone, email) values (8, 'Jeniffer Anderson', 'Nakuru', '555-555-5562', '.enniferanderson@email.com');
insert into customers (customer_id, name, address, phone, email) values (9, 'William Thompson', 'Mombasa', '555-555-5563', 'williamthompson@email.com');
insert into customers (customer_id, name, address, phone, email) values (10, 'Joseph Gonzalez', 'Nakuru', '555-555-5564', 'josephgonzalez@email.com');

USE mini_project;
CREATE TABLE Products (
    product_id VARCHAR(4) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

INSERT INTO Products (product_id, name, description, price) VALUES 
('p001', 'Airforce one', 'A high-quality product that is reliable.', 50.00),
('p002', 'Versace gumboots', 'A durable product that is built to last.', 75.00),
('p003', 'Swiss knife', 'A versatile product that can be used for many purposes.', 100.00),
('p004', 'Bamburi cement', 'A premium product that is made with the best materials.', 150.00),
('p005', 'Shuma ya doshi', 'A unique product that stands out from the rest.', 200.00),
('p006', 'Rolex watch', 'A budget-friendly product that is great value.', 25.00),
('p007', 'Google Pixel 7', 'A cutting-edge product that uses the latest technology.', 200.00),
('p008', 'Gucci handbag', 'A stylish product that looks great.', 125.00),
('p009', 'Fiber wrapping', 'An eco-friendly product that is good for the environment.', 75.00),
('p010', 'power saw', 'A high-performance product that delivers results.', 350.00);

DROP TABLE inventory;
CREATE TABLE inventory (
    warehouse_id VARCHAR(4) NOT NULL,
    product_id VARCHAR(4) NOT NULL,
    stock_quantity INT NOT NULL,
    PRIMARY KEY (warehouse_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO inventory (warehouse_id, product_id, stock_quantity) VALUES 
('w001', 'p001', 100),
('w002', 'p002', 50),
('w003', 'p003', 25),
('w004', 'p004', 10),
('w005', 'p005', 5),
('w006', 'p006', 75),
('w007', 'p007', 50),
('w008', 'p008', 30),
('w009', 'p009', 20),
('w010', 'p010', 110);

CREATE TABLE Orders (
    order_id VARCHAR(4) PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL
);

INSERT INTO Orders (order_id, customer_id, order_date, total_amount) VALUES 
('k001', 1, '2021-01-01', 100.00),
('k002', 2, '2021-01-02', 200.00),
('k003', 3, '2021-01-03', 150.00),
('k004', 4, '2021-01-04', 250.00),
('k005', 5, '2021-01-05', 300.00),
('k006', 6, '2021-01-06', 200.00),
('k007', 7, '2021-01-07', 400.00),
('k008', 8, '2021-01-08', 450.00),
('k009', 9, '2021-01-09', 500.00),
('k010', 10, '2021-01-10', 550.00);
