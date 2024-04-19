class Animal:
    def sound(self):
        print("Print generic sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Dog(Animal):
    def sound(self):
        print("woof")


mycat = Cat()
mydog = Dog()
mycat.sound()
mydog.sound()




class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return "Vehicle is moving"
    
class Car(Vehicle):
    def __init__ (self, brand, model):
        super().__init__(brand)
        self.model = model



vehicle, car = Vehicle("Generic Vehicle"),Car("Toyota","Corolla")

print(f"{vehicle.brand}\n{car.brand}\n{car.model}\n{vehicle.drive()}\n{car.drive()}")



