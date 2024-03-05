#\n means to add the input in the next line!

# input radius (area of circle)

radius = float(input("what is the radius?\n"))

# def area  
area_circle = 3.14159 * radius ** 2
print("The area is: ",area_circle)



# base and height (Area of a Triangle)

base = float(input("What is the base?\n"))
height = float(input("What is the height?\n"))

area_tri = 0.5*(base*height)
print("The area of the triangle is:", area_tri)


#Area of a square - optional extra i did in class to help you understand.
length = float(input("What is the length?\n"))
height = float(input("What is the height?\n"))

area_sqr = length * height
print("This is the area of the square:", area_sqr)

from math import sqrt
# Try Pythagoras - ill help, ive given the basics you have to fix and complete code! input math in sqrt() function to square root
x = input("What is the x value:\n")
y = input("What is the y value:\n")

hypoteneus = sqrt()

print(hypoteneus)

# Simple interest

Principle = 1000
rate = 0.05
time = 2
simple_int = Principle * rate * time
print("Simple interest:", simple_int)

Principle = float(input("Principles?"))
rate =float(input("Rate?"))
time = float(input("time?")) 
simple_int = Principle * rate * time
print("Simple interest:", simple_int)

#Feet to meters
meters = float(input("How many meters?\n"))

feet = meters * 3.281
print(feet,"Ft")

#inches to cm 
inches = float(input("How many inches?\n"))
cm = inches * 2.54

print(cm,"cm")
