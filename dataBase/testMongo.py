from pymongo import MongoClient
from globals import connStr
from bson import ObjectId

client = MongoClient(connStr) #Pass URL of mdb cluster
db = client.get_database('UsersTestDB')
coll = db.Users
'''print(coll.count_documents({}))

new_user = {
    'name': 'Alejandro',
    'lastName': 'Vasquez',
    'age': 22
}

coll.insert_one(new_user)'''

print(coll.count_documents({})) #Count number of documents in a collection

print(list(coll.find())) #Find all docs in a collection

 
print(coll.find_one({"name": "Alejandro"})) #Filter given a condition, note always use ""a

new_user = {
    'name': 'Zaida',
    'lastName': 'Vasquez',
    'age': 52
}

usrID = coll.insert_one(new_user).inserted_id #Insert into collection and get id

update_user = {
    'lastName': 'Vasquez Ramirez'
} #Properties to be changed

coll.update_one({"_id": ObjectId(usrID)}, {'$set': update_user}) #Update one. First query, then '$set' the properties 

print(coll.find_one({"_id": ObjectId(usrID)}))

coll.delete_one({"_id": ObjectId(usrID)}) #Delete one, always query
