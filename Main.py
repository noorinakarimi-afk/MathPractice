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
preferred_operation = input(" 1 - Addition"
                            " 2 - Subtraction"
                            " 3 - Multiplication"
                            " 4 - Division: ")
#Create random
x = random.randint(lowest_number, highest_number)
y = random.randint(lowest_number, highest_number)
x = x * y
answer = x//y
print(f"{x} {preferred_operation} {y}?: ")
if

print(f"{x} {preferred_operation} {y} = {answer}")

