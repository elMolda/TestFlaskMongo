from pymongo import MongoClient
from .globals import connStr
from models.User import User
from bson.json_util import dumps

client = MongoClient(connStr) 
db = client.get_database('UsersTestDB')
collection = db.Users

def getAllUsers():
    usrsLst = list(collection.find())
    sndUsrsLst = []
    for usr in usrsLst:
        addUsr = User(usr["name"], usr["lastName"], usr["age"])
        sndUsrsLst.append(addUsr.toDict())
    return sndUsrsLst
    