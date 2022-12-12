# Set the initial count to 1
count = 1

# Loop indefinitely
while True:
  # Print the current count
  print(count)

  # Increment the count
  count += 1

  # Prompt the user to enter the next number
  next_number = int(input("Enter the next number: "))

  # Check if the next number is correct
  if next_number == count:
    # Continue the loop if the number is correct
    continue
  else:
    # Print a message and exit the loop if the number is incorrect
    print("Sorry, that's not the correct number. The game is over.")
    break
