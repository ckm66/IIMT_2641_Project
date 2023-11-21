import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
load_dotenv()


database = MongoClient(os.getenv('CONNECTION_STRING')).get_database('Auction_Analysis')
collection = database['Auction_Records'].delete_many({})
invalid_collection = database['Auction_Records_Invalid'].delete_many({})