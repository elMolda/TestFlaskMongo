from .globals import *
from models.User import User
from mongoengine import *

'''client = MongoClient(connStr) 
db = client.get_database('UsersTestDB')
collection = db.Users'''

connect(db=dbName,host=connStr)

def getAllUsers():
    usrs = []
    for usr in User.objects():
        usrs.append(usr.to_json())
    return usrs