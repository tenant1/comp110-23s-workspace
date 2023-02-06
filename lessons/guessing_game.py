"""Ask user for number, give hints about number if wrong"""

SECRET: int = 10
guess: int = int(input("Guess a number! "))
playing: bool = True 

while playing: 
    if guess == SECRET:
        print("Correct! You did it! Believe in your dreams <3")
        playing = False
    else: 
        guess = int(("Wrong guess. Try again! "))
        