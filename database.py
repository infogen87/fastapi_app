
from pymongo import mongo_client

import os

from dotenv import load_dotenv

load_dotenv()

MONGO_DB_CONNECTION_URL = os.environ.get("MONGO_DB_CONNECTION_URL")

client = mongo_client.MongoClient(MONGO_DB_CONNECTION_URL)



user_collection = client["todo_app"]["users"]
todo_collection = client["todo_app"]["todos"]
