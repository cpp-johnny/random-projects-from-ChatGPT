import random

# Define the roulette wheel
wheel = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8,
         23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]

# Start the game loop
while True:
  # Prompt the user for their bet
  print("Roulette table:")
  print("0  32  15  19  4  21  2  25  17  34  6  27  13  36  11  30  8")
  print("23  10  5  24  16  33  1  20  14  31  9  22  18  29  7  28  12  35  3  26")
  print()
  print("Place your bet:")
  bet = int(input("Enter the number you want to bet on (0-36): "))

  # Check if the bet is valid
  if bet < 0 or bet > 36:
    print("Invalid bet. Please try again.")
    continue

  # Spin the roulette wheel
  result = random.choice(wheel)

  # Check if the player won or lost
  if result == bet:
    print("You won! The roulette landed on", result)
  else:
    print("You lost. The roulette landed on", result)

  # Ask the user if they want to play again
  answer = input("Do you want to play again? (y/n) ")
  if answer.lower() != "y":
    break

# End the game
print("Thanks for playing!")
