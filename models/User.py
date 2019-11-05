class User:
    def __init__(self, name, lastName, age):
        self.name = name
        self.lastName = lastName
        self.age = int(age)

    def toDict(self):
        dict = { 'name': self.name,
                 'lastName': self.lastName,
                 'age': self.age
                }
        return dict