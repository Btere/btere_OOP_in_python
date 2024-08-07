#overiding variables

from typing import List

class PolandCities:
    City1: str = "Gdansk"
    City2: str = "Krakow"


class SizeOfCites(PolandCities):
    City1: str = "Krakow"
    City2: str = "Gdansk" 


#overriding methood

class PolandCities:

    def cities_with_jobs(cites: str = "Warsaw"):
        if cites == "Krakow":
            return "cites"
        else:
            return "Gdansk"


class SizeOfCites(PolandCities):

    def cities_with_jobs(cites: str = "Warsaw"):
       #return super().cities_with_jobs()  #this allow us to call the method in the parent class,the super()
       return "ponanz"
    

#method overloading

class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{0} eats {1}".format(self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print("{0} goes after the {1}!".format(self.name, thing))

    def show_affection(self):
        print("{0} wags tail".format(self.name))


class Cat(Animal):
    def swatstring(self):
        print("{0} shreds more string".format(self.name))

    def show_affection(self):
        print("{0} purrs".format(self.name))


for a in (Dog("Rover"), Cat("Fluffy"), Cat("Lucky"), Dog("Scout")):
    print(a.show_affection())

#obj = SizeOfCites()
#obj2 = SizeOfCites()
#print(obj2.cities_with_jobs())
#print(obj.City2)
#obj3 = PolandCities()
#print(obj3.cities_with_jobs())
obj_animal = Animal("Rover")