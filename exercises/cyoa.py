"""EX06 - Choose Your Own Adventure."""

__author__ = "730489449"

import random

def main(): 
    global points, player, heart_eyes 
    points = 0
    player = ""
    heart_eyes = "\U0001F60D"
    greet()
    while True:
        print("Type one or two for a quiz and three to quit")
        choice = input("What would you like to do?")
        if choice == "1":
            procedure_1()
        elif choice == "2":
            points = procedure_2(points)
        elif choice == "3":
            print(f"You have {points} points goodbye!")
            break 
        else: 
            print("Invalid choice, try again!")

def greet():
    global player 
    print(f"Hello! {heart_eyes}")
    player = input("What is your name?")

def procedure_1():
    global player, points
    character = input(f"What Harry Potter character are you, {player}?")
    multiplier = random.randint(1,3)
    if character == "Harry": 
        points += 3*multiplier
    elif character == "Hermione":
        points += 5*multiplier
    elif character == "Snape":
        points += 2*multiplier
    elif character == "Draco":
        points += 4*multiplier
    else: 
        points += 1*multiplier

def procedure_2(number: int) -> int: 
    global player 
    character = input(f"Pick a number 1-5, {player}.")
    if character == "1":
        return number + 1 
    elif character == "2":
        return number + 2
    elif character == "3":
        return number + 3
    elif character == "4":
        return number + 4
    elif character == "5":
        return number + 5
    else: 
        return number 

if __name__ == "__main__": 
    main()

