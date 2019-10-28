class Person_2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #your code here
        self.pets = []
    def birthday(self):
        self.age += 1
        
    #your code here
    def add_pet(self, pet_type, pet_name):
        self.pets.append((pet_type, pet_name))
    
