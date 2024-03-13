#Question 1

Weathers_question = input("Dont know what to wear? whats the weather?\n1. Cold - wear a jacket.\n2. Hot - carry a water bottle.\n3. Rainy - Bring an umbrella.\n4. Windy - wear a windbreaker.\n5. Snowy - wear a  heavy coat.\n6. Sunny - wear sunscreen.\n")

if Weathers_question == "1" or Weathers_question.lower() == "cold":
    print("Wear a jacket")
elif Weathers_question == "2" or Weathers_question.lower() == "hot":
    print("Carry a water bottle")
elif Weathers_question == "3" or Weathers_question.lower() == "rainy":
    print("Bring an umbrella")
elif Weathers_question == "4" or Weathers_question.lower() == "windy":
    print("Wear a windbreaker")
elif Weathers_question == "5" or Weathers_question.lower() == "snowy":
    print("Wear a heavy coat")
elif Weathers_question == "6" or Weathers_question.lower() == "sunny":
    print("Wear sunscreen")
    
#Question 2
Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]



 
while True :  
    prompt = int(input("What is the number of the day?"))
    if prompt == 1:
        print(Days[0])
        False
    elif prompt == 2:
        print(Days[1])
        False
    elif prompt == 3:
        print(Days[4])
        False
    elif prompt == 4:
        print(Days[5])
        False
    elif prompt == 5:
        print(Days[6])
        False
    elif prompt == 6:
        print(Days[7])
        False
    elif prompt == 7:
        print(Days[8])
        False
    else:
        print("Invalid number!!")
        True
    break

    
#Question 3 


while True:
    operation = input("Choose operation (+, -, *, /) or 'exit' to quit: ")
    
    if operation == 'exit':
        print("Goodbye!")
        break
    
    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation!")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        add = num1 + num2
        print("Result:", add)
        True
    elif operation == '-':
        subtract = num1 - num2
        print("Result:", subtract)
        True
    elif operation == '*':
        multiply = num1 * num2
        print("Result:", multiply)
    elif operation == '/':
        divide = num1/num2
        if num2 == 0:
            print("Cannot divide with 0")
            True
        else:
     
         print("Result:", divide(num1, num2))
         True









