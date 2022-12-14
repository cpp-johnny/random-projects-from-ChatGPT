import random

# list of words to choose from
words = ["apple", "banana", "orange", "grape", "strawberry"]

# choose a random word
word = random.choice(words)

# initialize empty list for the correct letters
correct_letters = []

# initialize empty list for the incorrect letters
incorrect_letters = []

# initialize number of remaining guesses
remaining_guesses = 6

# initialize game over flag
game_over = False

while not game_over:
    # display current progress
    print("Word: ", end="")
    for letter in word:
        if letter in correct_letters:
            print(letter, end="")
        else:
            print("_", end="")
    print()

    # check if the player has won
    if all(letter in correct_letters for letter in word):
        print("You won!")
        break

    # check if the player has lost
    if remaining_guesses == 0:
        print("You lost!")
        break

    # ask for a letter
    letter = input("Guess a letter: ")

    # check if the letter is correct
    if letter in word:
        correct_letters.append(letter)
    else:
        incorrect_letters.append(letter)
        remaining_guesses -= 1

    # print remaining guesses
    print(f"Remaining guesses: {remaining_guesses}")

