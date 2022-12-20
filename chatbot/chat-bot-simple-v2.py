import random

# define a list of responses


responses = [
  'Hello!',
  'How are you?',
  "What's your name?",
  'Nice to meet you!',
  "How's your day going?",
  'What do you like to do in your free time?',
  "What's your favorite thing about Python?",
  'Do you have any hobbies or interests?',
  'Have you learned anything new today?',
  "What's your favorite thing about programming?",
  'Do you have any goals or aspirations?',
  "What's your favorite thing about computer science?",
  'What do you like most about technology?',
  "What's your favorite thing about the internet?",
  'Do you have any favorite websites or apps?',
  "What's your favorite thing about social media?",
  'Do you have any favorite video games or consoles?',
  "What's your favorite thing about movies or TV shows?",
  'Do you have any favorite books or authors?',
  "What's your favorite thing about music?",
  'Do you have any favorite bands or musicians?',
  "What's your favorite thing about sports?",
  'Do you have any favorite teams or players?',
  "What's your favorite thing about food?",
  'Do you have any favorite restaurants or recipes?',
  "What's your favorite thing about travel?",
  'Do you have any favorite destinations or landmarks?',
  "What's your favorite thing about nature?",
  'Do you have any favorite animals or plants?',
  "What's your favorite thing about science?",
  'Do you have any favorite subjects or fields of study?',
  "What's your favorite thing about history?",
  'Do you have any favorite events or periods?',
  "What's your favorite thing about art?",
  'Do you have any favorite artists or styles?',
  "What's your favorite thing about literature?",
  'Do you have any favorite poets or novels?',
  "What's your favorite thing about philosophy?",
  'Do you have any favorite philosophers or concepts?',
  "What's your favorite thing about psychology?",
  'Do you have any favorite theories or studies?',
  "What's your favorite thing about sociology?",
  'Do you have any favorite topics or researchers?',
  "What's your favorite thing about economics?",
  'Do you have any favorite concepts or models?',
  "What's your favorite thing about politics?",
  'Do you have any favorite parties or issues?',
  "What's your favorite thing about law?",
  'Do you have any favorite cases or principles?',
  "What's your favorite thing about education?",
  'Do you have any favorite teachers or subjects?',
  "What's your favorite thing about work?",
  'Do you have any favorite jobs or industries?',
  "What's your favorite thing about business?",
  'Do you have any favorite companies or entrepreneurs?',
  "What's your favorite thing about marketing?",
  'Do you have any favorite campaigns or strategies?',
  "What's your favorite thing about finance?",
  'Do you have any favorite investments or markets?',
  "What's your favorite thing about accounting?",
  'Do you have any favorite scientific discoveries or theories?',
  "What's your favorite thing about space?",
  'Do you have any favorite celestial bodies or phenomena?',
  "What's your favorite thing about physics?",
  'Do you have any favorite laws or principles?',
  "What's your favorite thing about chemistry?",
  'Do you have any favorite elements or compounds?',
  "What's your favorite thing about biology?",
  'Do you have any favorite organisms or processes?',
  "What's your favorite thing about geology?",
  'Do you have any favorite minerals or formations?',
  "What's your favorite thing about meteorology?",
  'Do you have any favorite weather patterns or phenomena?',
  "What's your favorite thing about astronomy?",
  'Do you have any favorite stars or galaxies?',
  "What's your favorite thing about engineering?",
  'Do you have any favorite technologies or inventions?',
  "What's your favorite thing about mathematics?",
  'Do you have any favorite formulas or theorems?',
  "What's your favorite thing about statistics?",
  'Do you have any favourite data sets or analyses?',
]


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
