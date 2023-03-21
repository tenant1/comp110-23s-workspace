"""EX06 - Choose Your Own Adventure."""

__author__ = "730489449"

import random
points: int = 0
player: str = ""
heart_eyes: str = "\U0001F60D"
def main(): 
    """Define a main function, that returns None, and follows the 
    Python idiom for calling main at the end of the program based 
    on the dunderscore variable __name__ being equal to "__main__".
    """
    greet()
    global points
    while True:
        print("Type one or two for a quiz and three to quit")
        choice: str = input("What would you like to do?")
        if choice == "1":
            procedure_1()
        elif choice == "2":
            points = procedure_2(points)
        elif choice == "3":
            print(f"You have {points} points goodbye!")
            break 
        else: 
            print("Invalid choice, try again!")

def greet() -> None:
    """
    The greet function must print a welcome message to give some context to your 
    game and asks the player for their name. 
    """

    global player 
    print(f"Hello! {heart_eyes}")
    player = input("What is your name?")

def procedure_1() -> None:
    """
    The procedure should lead to textual interaction(s) that make use of players 
    name and ask the player for additional input.
    """
    global player, points
    character = input(f"What Harry Potter character are you, {player}?")
    multiplier = random.randint(1,3)
    if character == "Harry": 
        points+=3*multiplier
    elif character == "Hermione":
        points+=5*multiplier
    elif character == "Snape":
        points+=2*multiplier
    elif character == "Draco":
        points+=4*multiplier
    else: 
        points+=1*multiplier

def procedure_2(number: int) -> int: 
    """
    The function takes at least one int as a parameter and returns an int. The call 
    to this function from main should pass the player’s points value as an argument to 
    the function call
    """
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