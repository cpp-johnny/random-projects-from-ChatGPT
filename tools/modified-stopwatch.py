import time

# Get the number to count down from and the delay between counts
count = int(input('Enter a number to count down from: '))
delay = int(input('Enter the number of seconds to delay between counts: '))

# Count down from the number
for i in range(count, 0, -1):
    # Print the number in block text
    print(f'{i} {"  "*(len(str(count)) - len(str(i)))}')
    
    # Pause for the specified number of seconds
    time.sleep(delay)

# Print "Blast off!"
print('Blast off!')
