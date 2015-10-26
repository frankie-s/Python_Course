class Bank:
    current_mammal = 0
    def __init__(self, age):
        self._hair = True
        self._quad_heart = True
        self._age = age
        self._warm_blooded = True
 
    def breathe(self):
        return "in, out"
 
class Cat(Bank):
    def __init__(self, name, breed, age):
        super().__init__(age)
        self._name = name
        self._breed = breed
        Bank.current_mammal = Bank.current_mammal + 1
        self._id_num = Bank.current_mammal
 
    def fetch(self):
        return "no"
 
    def breathe(self):
        return "You don't tell me what to do. In, out."
         
     
class Dog(Bank):
#    current_dog = 0
     
    def __init__(self, name, breed, age):
        super().__init__(age)
        self._name = name
        self._breed = breed
        self._bark = "Woof!"
        Bank.current_mammal = Bank.current_mammal + 1
        self._id_num = Bank.current_mammal
        self._tag = ""
        self._biscuits = 0
        self._toys = 0
         
    @property
    def kcred(self):
        return self._biscuits + (self._toys * .5)
 
    @property
    def tag(self):
        return self._tag
 
    @tag.setter
    def tag(self, tag):
        if 4 < len(tag) < 9:
            self._tag = tag
 
    @tag.deleter
    def tag(self):
        self._tag = ''
 
     
 
    def __str__(self):
        return str(self._id_num) + ', ' +str(self._name) + ', ' +str(self._breed) 
 
    def bark(self):
        return self._bark
 
    def fetch(self, thing):
        '''fetch(thing) -> string, thing should be a string'''
        return "Here's the thing " + str(thing)
 
class Kennel:
    def __init__(self, name, owner):
        self._name = name
        self._owner = owner
        self._dogs = []
