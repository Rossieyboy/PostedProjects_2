#Single inheritence

class Animals:
    def __init__ (self,name,age):
        self.name = name
        self.age = age


    def eat(self):
        print("The animal is eating...")

class Dog(Animals):
    def bark(self):
        print("Woof woof")

d = Dog("Rover",3)

print(d.name)
d.eat()
d.bark()

# Multiple inheritance

class Bird:
    def fly(self):
        print("The bird is flying")

class mammal:
    def run(self):
        print("The mammal is running")

class Bat(mammal,Bird):
    pass

bat = Bat()

bat.fly()
bat.run()
        

class Animal:
    def eat(self):
        print("The animal is eating")

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

class Poodle(Dog):
    def play_fetch(self):
        print("The poodle is playing fetch!")

poodle = Poodle()

poodle.eat()
poodle.bark()
poodle.play_fetch()