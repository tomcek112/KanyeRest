from pymongo import MongoClient


#THIS SCRIPT DROPS YOUR DATABASE!!!!!! USE WITH CAUTION!!!!

client = MongoClient()
db = client.kanye
db.kanye.drop()