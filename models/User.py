from mongoengine import *

class User(Document):
    email = EmailField(required=True)
    name = StringField(max_length=50)
    lastName = StringField(max_length=50)
    age = IntField(min_value=0)