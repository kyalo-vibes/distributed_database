# Distributed Database Mini Project

**Description**

We are to create a distributed database system that will be able to handle the following:
1) Have the relations/tables on all 3 sites
2) Each site, according to the frequency of access, allocated a report.
3) Short demo of running reports. 


**Requirements**

- 3 sites with three different participating database platforms
- At least 2 operating systems.
- At least 4 distributed relations
- Choose one of the sites to be the decision site and perform reconstruction using either views, functions, stored procedures or any other technique

**Distributed Relations:**
- Customers: Contains information about the customers of the company, such as name, address, and contact information.
- Orders: Contains information about the orders placed by customers, including the products ordered, the quantity of each product, and the total price.
- Products: Contains information about the products available for purchase, including the product name, description, and price.
- Inventory: Contains information about the current inventory levels of each product.

**Site Structure:**
-Site A - where vertical fragmentation takes place. Runs on local machine(Windows & MySQL)[DONE]
-Site B - where PHF takes place. Runs on VM(Linux & postgresql)[DONE]
-Site C - where DHF takes place. Runs on local machine(windows & MYSQL)[DONE]

## Running the App
-Run the following commands in the terminal and not in VSCode terminal.
-Create a virtual environment:
```bash
virtualenv project
```
-Activate the virtual environment:
```bash
flask\Scripts\activate
```
-Install relevant libraries using:
```bash
pip install mysql.connector
pip install pyscopg2
```
-Simply run and ensure the interpreter selected in VSCode is the flask venv:
```bash
siteAWindows.py
siteBLinux.py
siteCWindows.py
```

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### siteAWindows

The [site A](./siteAwindows.py) file contains a our implementation of virtual fragmentation using the all applications and their attributes and we create two fragments namely Q1 and Q2. The file contains the following:
1. `Connect to database`
2. `Perform vertical fragmentation`
3. `Display results`

> View the [siteAwindows](./siteAwindows.py) for more details.

### siteBLinux

The [site B](./siteBlinux.py) file contains a our implementation of primary horizontal fragmentation using the first application on the orders table and we create two fragments namely phf1 and phf2. SInce phf1 is mostly accessed in site B we keep it here and ship phf2 to windows machine and perform schema translation for it to sit in the MySQL database. The file contains the following:
1. `Connect to database`
2. `Perform horizontal fragmentation`
3. `Ship phf2 to windows machine as a python list`
4. `Perform schema translation`
5. `Display results`

> View the [siteBLinux](./siteBlinux.py) for more details.

### siteCwindows

The [site C](./siteCwindows.py) file contains a our implementation. We start with PHF to generate loc1 and loc2 from product table. Then derived horizontal fragmentation using products(loc1 and loc2) as owner table and inventory as member table and we create four fragments namely dhf1, dhf2, dhf3 and dhf4. Since dhf1 and dhf2 are accessed most here we keep in site C and ship dhf3 and dhf4 to site B. Since The file contains the following:
1. `Connect to database`
2. `Perform primary horizontal fragmentation`
3. `Perform derived horizontal fragmentation`
4. `Ship dhf3 and dhf4 to site B`
5. `Perform schema translation`
6. `Display results`

> View the [siteCwindows](./siteCwindows.py) for more details.

