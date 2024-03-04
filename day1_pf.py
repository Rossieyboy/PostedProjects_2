#Hello, this is the work we did on the 4th of march with proper variable names!!
greeting = "Hello World"
print(greeting)



#Looping in Python
count = 0 
while count < 5:
     print("Count: ", count)
     count += 1


if 5 > 2:
     print("five is greater than two")

x = 10
if x > 5:
     print("x is greater than 5")
else:
     print("x is less than 5 ")


#if you want to specify the data typw of a variable, this can be done with casting
p = str(3) # p will be "3"
q = int(3) # q will be 3 
r = float(3) # r will be 3.0

#get the type 
g = 5
h ='john'
print(type(g))
print(type(h))


#Case Sensitivity 
# this will create two variables

v = 4
V = "Sally"
#V will not overwrite v ( Case sensitve )

#(1)Camel Case:

myvariableName = "John"

#(2)Pascal Case:

MyVariable = "John"

#(3)Snake Case 

My_Variable_Name = "John"


#Python Allows to assign to multiple values

g,y,z = "pear","grape","apple"

#assign multiple variables to one value

e = f = v = "Orange"

#Print()
i = "python"
o = "is"
l = "Great"

print(i,o,l)

#print( using plus)
B = "i got this feeling" 
M = "inside my bones"
n = "!!!!"
print(B+M+n)

#Global Variable
y = "awesome"
def myfunc():
     print("Python is " + y)

myfunc()     

#global and local variable
j = "Simple"

def myfunc1():
     j = "Fantastic"
     print("Python is " + j)

myfunc1()
print("Pyton is " + j) #calls simple
myfunc1() #calls fantastic


#using the global keyword
def myfunc2():
     global i
     i = "amazing"
myfunc2()

print("Python is " + i)


#Setting python datatypes
x1 = "Hello World"
x2 = 20
x3 = 20.5
x4 = 1j
x5 = ["Apple","Banana","Cherry"]
x6 = ("Apple","Banana","Cherry")
x7 = range(6)
x8 = [{"Name" : "John", "Age" : 36}]
x9 = {"Apple","Banana","Cherry"}
x10 = frozenset({"Apple","Banana","Cherry"})
x11 = True
x12 = b"hello"
x13 = bytearray(5)
x14 = memoryview(bytes(5))
x15 = None

x01 = str("Hello World")
x02 = int(20)
x03 = float(20.5)
x04 = complex(1j)
x05 = list(("Apple","Banana","Cherry"))
x06 = tuple(("Apple","Banana","Cherry"))
x07 = range(6)
x08 = dict(name = "John", age = 36)
x09 = set(("Apple","Banana","Cherry"))
x010 = frozenset({"Apple","Banana","Cherry"})
x011 = bool(5)
x012 = bytes(5)
x013 = bytearray(5)
x014 = memoryview(bytes(5))
 




import random

print("The number generated is ", random.randrange(1,10))

#slicing strings certain range

B1 = "Hello World!"
print(B1[2:5])

#slicing from start
print(B1[:6])

#Slicing from end

print(B1[2:])

#Negative indexing
print(B1[-5:-2])

#Negative indexing from start
print(B1[:-8])

#Negative indexing from end
print(B1[-1:])

#Modifying strings
#THE UPPER
a1 = "hello, world!"
print(a1.upper())
#the lower
print(a1.lower())
#title
print(a1.title())
#Strip - removes alpha & omega white space
a2 = " Hello, world!  "
print(a2.strip())
#The replace
print(a1.replace("H","J"))
#Split
print(a1.split(","))

#Concatenate
t1 = "Hello "
t2 = " World"
t_ans = t1 + t2 
print(t_ans)


#The split() method splits the string into substrings
a3 = "Hello, World!"
print(a3.split(",")) # returns ["Hello", "World"]

#Python Boolean

r1,r2 = 200,33

if r2 > r1 :
     print("r1 is greater than r2")
else:
     print("r1 is not greater than r2")

r3,r4 = random.randrange(1,100),random.randrange(1,100)
if r3 > r4 :
     print("r4 is greater than r3")
else:
     print("r4 is not greater than r4")



#operators
number1 , number2, number3 = 5,5,10
print(number1 is number2)# check if number1 = number2
print(number1 is not number3) #check if number1 /= number3