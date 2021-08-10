from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

client = MongoClient()
db = client.get_database(os.getenv('MONGODB_URL'))
