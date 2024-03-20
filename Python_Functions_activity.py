#Calculator

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1 / num2

while True:
    prompt_1 = int(input("Choose an operation\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n=> "))

    if prompt_1 in [1, 2, 3, 4]:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))

        if prompt_1 == 1:
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif prompt_1 == 2:
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif prompt_1 == 3:
            print(f"{num1} x {num2} = {multiply(num1, num2)}")
        elif prompt_1 == 4:
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        prompt_2 = input("Would you like to do another operation? (Y/N)\n=> ")
        if prompt_2.lower() == "n":
            break
        elif prompt_2.lower() != "y":
            print("Invalid input! Exiting...")
            break
    else:
        print("Invalid operation choice! Exiting...")
        break


#Factorial

def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n - 1)
    

prompt = int(input("Input a number\n=> "))

ans = Factorial(prompt)
print(f"The factorial is: {ans}")

#Palindrome 

def is_palindrome(word):
    word = "".join(char.lower() for char in word if char.isalnum())
    return word == word[::-1]

word = input("What is your word?")

if is_palindrome(word):
    print("palindrom")
else:
    print("not palindrom")

#Quadratic Equation Solver

from math import sqrt

a,b,c = int(input("What is A:")),int(input("What is B:")),int(input("What is C:"))

ans_1,ans_2 = (-b + sqrt(b**2 - 4*a*c)/2*a),(-b - sqrt(b**2 - 4*a*c)/2*a)

print(f"For values {a}, {b}, {c}:\nx = {ans_1} or x = {ans_2}")

#fibonacci
def fibonacci(n):
    fib_seq = [0,1]

    if n <= 0:
        return "Please enter a positive integer"
    elif n == 1:
        return[0]
    elif n==2:
        return fib_seq
    
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
     
    return fib_seq


n = int(input("What is your range?"))

print(f"Sequence is : {fibonacci(n)}")

#Temp Converter
def Celcius_to_fahren(x):
    ans = (x * (9/5)) + 32
    return ans

def fahren_to_celcius(x):
    ans  = (x - 32) * (5/9)
    return ans


prompt = int(input("Would you like to convert\n1. (°C to °F)\n2. (°F to °C)\n"))

if prompt == 1:
    celcius = float(input("input °C\n"))
    ans = Celcius_to_fahren(celcius)
    print(f"{celcius}°C to {ans}°F")
    prompt





elif prompt == 2:
    fahrenheit = float(input("input °F\n"))
    ans = fahren_to_celcius(fahrenheit)
    print(f"{fahrenheit}°C to {ans}°F")
    prompt