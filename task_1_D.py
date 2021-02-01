import pandas
import json
from pymongo import MongoClient

df = pandas.read_csv('/var/lib/mysql-files/test.csv', names=("1", "2", "3", "4", "5", "6"))
df.to_json('generated.json', orient='records')

myclient = MongoClient("mongodb://localhost:4000/")
db = myclient["recordsDb"]
Collection = db["records"]
with open('generated.json') as file:
    file_data = json.load(file)
if isinstance(file_data, list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)

query = {"3": {"$regex": "^[a-zA-Z]"}}

db.delete_many(query)
