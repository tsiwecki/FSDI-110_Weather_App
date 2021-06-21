# description
"""
PyCalc: Simple Calculator

Author: Thadeus Siwecki

Date: June 2021

Course: FSDI 110
        Introductory Python

Learning Outcomes
    -Install Python
    -Learn how to create python scripts
    -Learn how to execute python scripts

Assignment 1 - Class 1 
    -Simple Python calculator
    (Please deliver the simple python calc, it should present the user with the following  (all the menu options should be working):
        1 - Sum
        2 - Subtract
        3 - Multiplication
        4 - Division
        5 - Is it odd ?
        6 - Print a message N times

Functionality:
    - Simple mathmatical operations (sum, subtraction, multiplication, division)
"""

# imports

# globals

# functions
def print_menu():
    print("--------------------")
    print(" Welcome to my PyCal")
    print("--------------------")

    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")    
    print("4 - Division")
    print("5 - Is a number odd")
    print("6 - Print a message")
    print("\nYOU CANNOT MULTIPLY OR DIVIDE BY ZERO.....AN ERROR WILL OCCUR!!!")
    
    print("\nq - Quit")

    print("--------------------")

def clear():
    print("\n\n\n\n\n")


# instructions
selected_option = ""
while(selected_option != "q"):
    clear()
    print_menu()

    selected_option = input("Select an option:  ")

    if(selected_option == "q"):
        break    

    if(int(selected_option) <5):

        num1 = float(input("Enter number 1:  "))
        num2 = float(input("Enter number 2:  "))
        
    if(selected_option == "1"):    
        res = num1 + num2
        print(f"The result is:  {res}")

    elif(selected_option == "2"):
        res = num1 - num2
        print(f"The result is:  {res}")

    elif(selected_option == "3"):
        res = num1 * num2
        print(f"The result is:  {res}")

    elif(selected_option == "4"):
        if(num2 == 0):
            print("Error: Division by ZERO is NOT allowed!!")
        else:
            res = num1 / num2
            print(f"The result is:  {res}")  

    if(selected_option == "5"):
        res = int(input("Enter any number: "))
        flag = res%2

        if flag == 0:
            print(f"This is an even number:    {res}")

        if flag == 1:
            print(f"This is an odd number:    {res}")

    if(selected_option == "6"):
        times = input("How many times would you like to repeat your message?")
        word = input("Enter your message:  ")
        print('\n'.join([word] * int(times)))         


    input("\nPress Enter to continue......") # will hold the execution until the user presses enter....it's a pause

print("\nGood byte!!")

    