#  Activity 2

class Rectangle:
    def __init__(self,width,length):

        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width


#Used a input instead of a set value to make it better    
rectangle = Rectangle(float(input("What is the length?\n")),float(input("What is the width?\n")))

print(f"Area of rectangle : {rectangle.area()}")
        

#Activity 3

class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def show_info(self):
        print(f"Make : {self.make}\nModel : {self.model}") 


Car1,Car2,Car3 = Car("Toyota" , "Corolla"),Car("Honda" , "Civic"),Car("Ford","Mustang")

print("Car 1:")
Car1.show_info()

print("Car 2:")
Car2.show_info()

print("Car 3:")
Car3.show_info()

# Activity 4

class Bank_account:
    def __init__(self,Account_number,Account_holder_name,initial_balance = 0):

        self.acc_num = Account_number
        self.acc_name = Account_holder_name
        self.ini_bal = initial_balance

    def Deposit(self, amount):

        self.ini_bal += amount
        print(f"Deposited ${amount}.\n Current balance {self.ini_bal} ")

    def withdraw(self,amount):
        if amount < self.ini_bal:
        
            self.ini_bal -= amount
            print(f"${amount} was withdrawn. \n Current balance is : {self.ini_bal} ")
        
        else:
            print(f"Insufficient funds.\n${self.ini_bal} is the active balance")

    def display_balance(self):
        print(f"Account Number: {self.acc_num}\nAccount Holder: {self.acc_name}\nCurrent Balance : ${self.ini_bal}")


Account1, Account2, Account3,Account4 = Bank_account(585425488,"Mercolm Goliath", 200),Bank_account(69865488,"Adam Mezichel", 1000),Bank_account(545154238,"Zaid Moses", 0),Bank_account(54515488,"Ross Solomons", 100)

Account1.display_balance()
Account1.Deposit(200)
Account1.withdraw(150)
Account1.display_balance()
            
Account5 = Bank_account(85456468,input("Enter Account Holder Name and Surname"),float(input("Enter an initial balance")))
Account5.display_balance()


class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "woof"
    

animal = Animal("Generic Animal")
dog = Dog("Buddy")

print(animal.name,dog.name,dog.speak())

