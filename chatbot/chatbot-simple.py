import random

# define a list of responses
responses = ['Hello!', 'How are you?', 'What is your name?', 'Goodbye!']

# define a variable to control the chatbot loop
running = True

# start the chatbot loop
while running:
  # get user input
  message = input("Enter a message: ")

  # check if the user wants to quit
  if message == 'quit':
    running = False
  else:
    # choose a random response from the list
    response = responses[int(random.random() * len(responses))]
    # print the response
    print(response)
