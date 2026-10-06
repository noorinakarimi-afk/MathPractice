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

#Loop and create random numbers
x = random.randint(lowest_number, highest_number)
y = random.randint(lowest_number, highest_number)
#Give problems to solve
if preferred_operation == "1":
    preferred_operation = "Addition"
for question in range(1, number_of_questions + 1):
    print(f"question {question}: {x} + {y} = ?")
    user_answer = int(input())
    
    if user_answer == answer:
        print("Good job!")
    else:
        print("Wrong! The answer is", answer)










