from pymongo import MongoClient
from . import models

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client.SamanthaRehomeDB  # Replace with your database name
users_collection = db.users # Replace with your collection name