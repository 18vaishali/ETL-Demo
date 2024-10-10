import pandas as pd
from pymongo import MongoClient

client= MongoClient('mongodb+srv://vaishalipasrija:admin0123456@cluster0.bcdar.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['db1']
collection = db['youtube']
document = {"name":"admin"}
"""insert_document = collection.insert_one(document)
print("Successfully inserted")
client.close()"""
data = pd.read_csv("C:/Users/SMS/Downloads/simple-zipcodes.csv")
sorted = data.sort_values(by=['Country'])
just_filters = data.filter(['Country','City','Zipcode','State'])
remove_dups = data.drop_duplicates()
jsondata = data.to_dict(orient='records')
collection.insert_many(jsondata)
print(sorted)
client.close()