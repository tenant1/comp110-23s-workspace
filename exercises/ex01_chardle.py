"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730489449"

term: str = input("Enter a 5-letter word:")
if len(term) != 5: 
    print("Error: Word must contain 5 letters")
    exit()
letter: str = input("Enter a single letter:")
if len(letter) > 1:
    print("Error: Letter must be a single letter.")
    exit()
matching_indices: int = 0
print("Searching for" + letter + "in" + term)
if letter == term[0]:
    print(letter + " found at index 0")
    matching_indices += 1
if letter == term[1]:
    print(letter + " found at index 1")
    matching_indices += 1
if letter == term[2]:
    print(letter + " found at index 2")
    matching_indices += 1
if letter == term[3]:
    print(letter + " found at index 3")
    matching_indices += 1
if letter == term[4]:
    print(letter + " found at index 4")
    matching_indices += 1
if matching_indices == 0: 
    print("no instances of " + letter + " found in " + term) 
if matching_indices == 1:
    print("1 instance of " + letter + " found in " + term)
if matching_indices >= 2: 
    print((str)(matching_indices) + " instances of " + letter + " found in " + term)
