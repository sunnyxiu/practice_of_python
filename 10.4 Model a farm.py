# -*- coding: utf-8 -*-
# round i: only stops at every ith cat and change their states 
class Animal:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
class Cat(Animal):
    def __init__(self, name, gender, age, fur_color):
        super().__init__(name, gender, age)
        self.fur_color = fur_color
    
    def relax(self):
        return f"{self.name} is purring."
    
class Dog(Animal):
    def __init__(self, name, gender, age, sound = "Woof"):
        super().__init__(name, gender, age)
        self.sound = sound        
    
    def relax(self):
        return f"{self.name} is rolling on its back."

class Rabbit(Animal):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)

    def relax(self):
        return f"{self.name} is flopping."

kitty = Cat("Kitty", "Female", 2, "white")
snoopy = Dog("Snoopy", "Male", 5)
miffy = Rabbit("Miffy", "Female", 1)

print(kitty.relax())
print(snoopy.relax())
print(miffy.relax())