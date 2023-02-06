"""EX02 - One-Shot Wordle - Loops."""

__author__ = "730489449"

# define secret word 
word = "python"
word_length = len(word)
# prompt user to input guess
term: str = input(f"What is your {word_length} -letter guess: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

continued = True
while (continued): 
    if len(term) != word_length:
        term = input(f"That was not {word_length} letters! Try again: ")
    else: 
        # establish a variable to keep track of the index of the word you are checking and initialize it to the first index of a string
        index = 0

        # establish a variable to store the resulting emoji of the guess and initialize it to an empty string.
        guess = ""

        # While the index variable is less than the length of the secret word
        while (index < word_length):
            # Test to see if the current index of the guessed word is equal to the same index of your secret word
            if (word[index] == term[index]): 
                # concatenate a GREEN_BOX emoji to the result string variable you setup previously
                guess = guess + GREEN_BOX 
            else:
                # Declare a boolean variable to keep track of whether the guessed character exists anywhere else in the word and initialize it to False.
                character_guessed = False
                # Declare a variable to keep track of the alternate indices of the secret you are checking for a match and initialize it to 0. 
                alternate_index = 0
                # Write while loop with the following test logic: while the boolean variable is not true and the index is less than the length of the secret
                while ((character_guessed is False) and (alternate_index < word_length)):
                    # Test to see if the alternate index of the secret word is equal to the current index of the guessed word.
                    if (word[alternate_index] == term[index]): 
                        character_guessed = True 
                    # Otherwise, increment your alternate index variable.
                    else:
                        alternate_index += 1
                
                if (character_guessed is True):
                    guess = guess + YELLOW_BOX 
                else: 
                    # concatenate a WHITE_BOX emoji
                    guess = guess + WHITE_BOX
            index += 1
        
        print(guess)
        if (word == term):
            print("Woo! You got it!")
        else:
            print("Not quite. Play again soon!")
        
        continued = False
