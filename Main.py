#Begin writing your code
import random

print("Welcome to Math practice. Let's get you started!")
#Ask for the amount of questions the user wants
number_of_questions = int(input("How many questions would you like?: "))
#Ask for the highest number
highest_number = int(input("What is the highest number?: "))
#Ask for the lowest number
lowest_number = int(input("What is the lowest number?: "))
#Ask for the user's preferred operation
print("What operation would you like to do?")
print(" 1 - Addition")
print("2 - Subtraction")
print(" 3 - Multiplication")
print("4 - Division: ")
preferred_operation = input("")
score = 0
#Loop
for question in range(1,number_of_questions+1):
#Create random numbers
    x = random.randint(lowest_number,highest_number)
    y = random.randint(lowest_number,highest_number)
#Calculate answers and determine the preferred operations
    if preferred_operation == "1":
        operation = "+"
        answer = x + y
    elif preferred_operation == "2":
        symbol = "-"
        answer = x - y
    elif preferred_operation == "3":
        operation = "*"
        answer = x * y
    elif preferred_operation == "4":
        operation = "//"
        x = x * y
        answer = x//y
#Give problems for user to solve
    user_answer = int(input(f"{question}: {x} {operation} {y}"))
#Check if the user's answer is correct
    if user_answer == answer:
        print("Good job!")
        score = score + 1
    else:
        print("Wrong! The answer is", answer)
#print the final score after the end of the loop
print(f"Your score is: {score}/{number_of_questions}")
print("Thank you for using Math practice!")











