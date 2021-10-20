# MongoDB
# Python can be used in database applications.

# One of the most popular NoSQL database is MongoDB.

# MongoDB
# MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable.


# PyMongo
# Python needs a MongoDB driver to access the MongoDB database.

# In this tutorial we will use the MongoDB driver "PyMongo".

# We recommend that you use PIP to install "PyMongo".

# PIP is most likely already installed in your Python environment.

# Navigate your command line to the location of PIP, and type the following:

# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install pymongo

# Test PyMongo
# To test if the installation was successful, or if you already have "pymongo" installed, create a Python page with the following content:

# import pymongo

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]