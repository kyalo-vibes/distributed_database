-Run siteAlinux - where vertical takes place. Runs on local(Windows & MySQL)[DONE]
-Run siteBwindows - where PHF takes place. Runs on VM(Linux & postgresql)[DONE]
-Run siteCwindows - where DHF takes place. Runs on local machine(windows & MYSQL)[DONE]

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
```

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### siteAWindows

The [site A](./siteAwindows.py) file contains a our implementation of virtual fragmentation using the first application on the orders table and we create two fragments namely Q1 and Q2. The file contains the following:
1. `Connect to database`
2. `Perform vertical fragmentation`
3. `Display results`

> View the [notebook](./lightgbm_model.ipynb) for more details.

### App

The [app](./app.py) file contains a FLASK application serving a RESTful API that will consume user input from a Flutter frontend and call the featureEngineering file. The predict API does the follwing:

1. Takes user input from the form in the frontend.
2. Creates a dataframe of all possible combinations with the columns `date, store, item, sales`.
3. Calls the `featureEngineering` module to generate features using `input_data.csv`.
4. Imports the `final_model.pkl` and passes the input to the model to perform prediction.
5. Returns a json object with tht prediction.


> View the [app](./app.py) for more details.

### featureEngineering

The [featureEngineering](./featureEngineering.py) app takes in `input_data.csv` and performs feature engineering to the user input has the same number of features as the ones used when training the model.

1. Takes user input from the Flask API.
2. Generates features so that `input_data` has 25 features that model expects.
3. Produces `X_test_final` that the Flask API will use to perform prediction.

> View the [featureEngineering](./featureEngineering.py) for more details.

### gain

The [gain](./gain.py) file contains the gain value which it obtains from the training dataset to trim features generated down to the 25 important features the model expects.

1. Takes training dataset.
2. Creates features using the dataset.
3. Calculates gain of the features using the `first_model`.
4. Outputs the gain to `featureEngineering`.

> View the [gain](./gain.py) for more details.
