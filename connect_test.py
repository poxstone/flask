import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.local
collection = db.maps
ll = collection.find({})
print dir(ll)