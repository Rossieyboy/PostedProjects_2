#Nature if number
num = int(input("What is the number?\n"))

if num > 0:
    print("Number is positive!")
elif num < 0 :
    print("Number is negative!")
else:
    print("Number is 0!")
    
#Student marks 
marks = float(input("What is the mark out of 100?\n"))

if marks > 100 or marks < 0:
    print("Invalid Mark")
elif marks > 74 and marks < 101:
    print(marks,"% Distinction")
elif marks < 75 and marks > 59:
    print(marks,"% Merit")
elif marks > 49 and marks < 60:
    print(marks,"% Pass")
else:
    print("Fail!")     
    
#Age groups 
age= int(input("What is your age\n"))

if age < 0:
    print("Invalid age")
    age 
elif age > 0 and age < 13:
    print("Child")
elif age > 12 and age < 20:
    print("Teenager")
elif age > 19 and age < 35:
    print("Youth")
elif age > 34 and age < 65:
    print("Adult")
else :
    print("Senior")  
    
#Even or odd
number = float(input("Your number is?\n"))

if number%2 == 0:
    print(number,"is even")
else:
    print(number,"is odd")