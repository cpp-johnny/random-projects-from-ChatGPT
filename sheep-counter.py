# Initialize the sheep counter
sheep_count = 0

# Start the sheep counter
while True:
    # Increment the sheep counter
    sheep_count += 1

    # Print the current count
    print(sheep_count)

    # Ask the user if they want to count another sheep
    response = input('Count another sheep? (y/n) ')

    # If the user doesn't want to count another sheep, break out of the loop
    if response.lower() != 'y':
        break

# Print the final sheep count
print('Total sheep counted:', sheep_count)





