from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(
    MONGO_URL,
    serverSelectionTimeoutMS=5000
)

db = client["synclogue"]

collection = db["users"]