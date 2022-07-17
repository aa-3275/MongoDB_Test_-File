import pymongo
client = pymongo.MongoClient("mongodb+srv://alok_10:mongodb@cluster0.wkm4q.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={ "name":"Alok","email": "alok@gmail.com","surname": "Singh"}
db1=client["mongotest"]
coll=db1["test"]
coll.insert_one(d)