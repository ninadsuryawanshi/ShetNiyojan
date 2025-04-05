from decouple import config
from pymongo import MongoClient

MONGO_URI = config("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client['shetniyojan']

users_collection = db['users']
tasks_collection = db['tasks']
