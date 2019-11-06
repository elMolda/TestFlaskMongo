from .globals import *
from models.User import User
from mongoengine import *
from flask import request

'''client = MongoClient(connStr) 
db = client.get_database('UsersTestDB')
collection = db.Users'''

connect(db=dbName,host=connStr)

def addOneUser(reqData):
    newUsr = User.from_json(str(reqData.json).replace("'","\""))
    newUsr.save()
    print(newUsr.id)
    if newUsr.id:
        return True
    else:
        return False