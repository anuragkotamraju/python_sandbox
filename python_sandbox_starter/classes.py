# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
class User:
    def __init__(self,name, age, email):
        self.name=name
        self.age=age
        self.email=email
    
    def greeting (self):
        return f'My name is {self.name} and I am {self.age}'
    
    def bDay(self):
        self.age+=1
class Customer (User):
    def __init__(self,name, age, email):
        self.name=name
        self.age=age
        self.email=email
        self.balance=0
    def set_balance(self, balance):
        self.balance=balance
    def greeting (self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

anurag = User('Anurag',25, 'anurag@gmail.com')
jane = Customer('Jane',26,'janet@gmail.com')
jane.set_balance(500)
anurag.bDay()
print(jane.greeting())