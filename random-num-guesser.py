import random

# Generate a random number between 1 and 100
correct_number = random.randint(1, 100)

# Ask the player to guess the number
guess = int(input("Guess the number: "))

# Set the number of attempts to 1
attempts = 1

# Loop until the player's guess is correct or they run out of attempts
while guess != correct_number and attempts < 10:
  if guess > correct_number:
    # If the player's guess is too high, give them a hint
    print("The number is lower than your guess.")
  else:
    # If the player's guess is too low, give them a hint
    print("The number is higher than your guess.")

  # Ask the player to guess again
  guess = int(input("Guess the number: "))

  # Increment the number of attempts
  attempts += 1

# Check if the player has won or lost
if guess == correct_number:
  # If the player's guess is correct, end the game and congratulate them
  print("Congratulations! You guessed the correct number.")
else:
  # If the player has run out of attempts, end the game and tell them the correct number
  print("Sorry, you ran out of tries")
