# prompt the user to enter the set of inputs
inputs_str = input("Enter the set of inputs, separated by commas: ")

# split the string into a list of inputs
inputs = inputs_str.split(',')

# prompt the user to enter the letter to search for
letter = input("Enter the letter to search for: ")

# initialize a list to store the results
results = []

# iterate through the inputs
for input in inputs:
  # check if the letter is in the input
  if letter in input:
    # if it is, add the input to the results list
    results.append(input)

# print the results
print(results)
