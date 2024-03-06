#Car Name
Car_Name = "Volvo"
print(Car_Name)

#Data types
integer = int(input("What integer you want?\n"))
floating = float(input("What floating point?\n"))
string = str(input("input a string\n"))
boolean = bool(input("True or False"))
print("the integer is:", integer,"\n", "The float is:", floating, "\n", "The string is:", string, "The boolean is:", boolean)

#Name and age
Name = input("What is your name?\n")
age = input("What is your age\n")

print("My name is",Name,"and I am ", age, "years old")

#Area calculator
x,y = 0,0

Question = input("What would you like the area of?\n")

if Question.lower() == "circle":
    x = float(input("What is the radius?"))
    area_circle = (3.14159 * x**2)
    print(area_circle)
elif Question.lower() == "square":
    x = float(input("What is the length?"))
    area_square = x**2
    print(area_square)
elif Question.lower() == "triangle":
    x = float(input("What is the length?"))
    y = float(input("What is the Height?"))
    area_triangle = 0.5*(x*y)
    print(area_triangle)
elif Question.lower() == "rectangle":
    x = float(input("What is the length?"))
    y = float(input("What is the Height?"))
    area_rect = x*y
    print(area_rect)       


# calculate simple interest 
principal, rate, time = float(input("What is the principle?\n")),0.05,float(input("What is the time in years?\n"))
Simple_int = principal * time* rate 
print("Your Simple interest is:",Simple_int)

#Quadratic
x=0

a,b,c = float(input("What is a?")),float(input("What is b?")),float(input("What is c?"))

from math import sqrt

answer_plus,answer_minus = 0,0

answer_plus = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
answer_minus = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
print("x =",answer_plus, "or", "x =", answer_minus)