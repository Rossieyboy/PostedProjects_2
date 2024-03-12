# For loop

for num in range(1,11):
    print(num)
    
# While loop

num = 1

while num < 11:
    print(num)
    num += 1
    
# Do while (No built in function for python)/while true
Condition = True
nomber = 0

while nomber < 11:
    print(nomber)
    nomber += 1
    Condition == False
    

# Sum of numbers

numbers = range(1,101)

Numbers_sum = sum(numbers)
print("The sum of numbers:",Numbers_sum)

#Gueesing game
import random

rand_num = random.randint(1,50)
my_num = int(input("What is the number?\n"))

if my_num == rand_num:
    print("You are correct my number is",rand_num)
elif my_num > rand_num:
    print("My number is less than yourssss")
    print(rand_num)
elif my_num < rand_num:
    print("My number is greater than yours")
    print(rand_num)

# Factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
n = int(input("what is your number?"))
print(factorial(n))