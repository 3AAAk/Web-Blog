from pymongo import MongoClient

# create a connection to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

db = client["web-blog"]

users_collection = db["user"]