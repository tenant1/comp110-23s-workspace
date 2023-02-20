"""EX03 - Structured Wordle"""

__author__ = "730489449"

"""
The purpose of this function is when given two strings, the 
first of any length, the second a single character, it will 
return True if the single character of the second string is
 found at any index of the first string, and return False 
 elsewhere.

 Parameters:
 word: string that is being searched through for the second 
 parameter
 character: string that is expected to be a single character
 in length and is the character being searched for 

 Returns:
 boolean denoting True if character is contained in string 
 or False if character is not contained in string 
"""
# define a function named contains_char
def contains_char(word: str, character: str) -> bool: 
    assert len(character) == 1
 # assert the assumptions that if an error will raise if found not to be true 
    length = len(word)
    index = 0
    while index < length:
        if (word[index] == character[0]): 
            return True 
        index = index + 1
    return False 

"""
The purpose of this function is if given two strings of equal 
length, the first a guess and then second a secret, it will return
a string of emoji whose color codifies as necessary in wordle.

Parameters:
guess: string representing user's guess
secret: string representing secret word 

Returns: string of emojis in coding user's guess
"""
# declare a function named emojified 
def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    # use this assertion since anyone using this function will provide strings of equal length
    # reuse the named constants you setup in EX03 for the colored emoji boxes
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    guess_box = ""
    length = len(guess) 
    index = 0
    while index < length:
        if (guess[index] == secret[index]): 
            # concatenate a GREEN_BOX emoji to the result string variable you setup previously
            guess_box = guess_box + GREEN_BOX 
        else:
            contained = contains_char(secret, guess[index])
            if (contained is True):
                guess_box = guess_box + YELLOW_BOX 
            else: 
                # concatenate a WHITE_BOX emoji
                guess_box = guess_box + WHITE_BOX 
        index = index + 1 

    return guess_box

"""
Purpose: Given an integer named "expected length" of a guess as a 
parameter, a prompt will appear for the user and continue promting
until provided with a guess of the expected length.

Parameters:
expected_length: integer expected length of a guess

Returns: guess of appropriate length 
"""
# define a function named input_guess
def input_guess(expected_length: int) -> str:
    # prompt user to input guess
    term: str = input(f"Enter a {expected_length} character word: ")
    continued = True
    while (continued): 
        if len(term) != expected_length:
            term = input(f"That wasn't {expected_length} chars! Try again: ")
        else: 
            return term
"""
 the purpose of the main function is to establish what 
 the secret word is as a variable 
 the main function will have no parameters and will return none
"""
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret = "codes"
    correct_length = len(secret) 
    turn = 1
    while turn <= 6: 
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(correct_length)
        answer = emojified(guess, secret)
        # Print the current turn number in a format such as === 
        # Turn 1/6 ===
        print(answer)
        # Prompt the user for a guess, relying on your function 
        # input_guess to obtain a guess of the correct length.
        if (guess == secret):  
            # Codify the emoji results of the user’s guess versus 
            # the secret by making use of your emojified function. 
            # Print the resulting codified string.
            print(f"You won in {turn}/6 turns!")
            break
        else: 
        # Otherwise, when the user does not guess the word 
        # in 6 or fewer guesses,
            if (turn == 6): 
                print("X/6 - Sorry, try again tomorrow!")

            turn = turn + 1

# Add the following snippet of code as the last 2 lines of your 
# program
if __name__ == "__main__":
    main()
