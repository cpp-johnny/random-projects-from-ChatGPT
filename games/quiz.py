questions = [
    "What is the capital of France?",  # question 1
    "What is the currency of Japan?",  # question 2
    "Who is the current President of the United States?",  # question 3
    "What is the capital of Italy?",  # question 4
    "What is the largest ocean in the world?",  # question 5
    "Who wrote the book 'To Kill a Mockingbird'?",  # question 6
    "Who invented the telephone?",  # question 7
    "What is the highest mountain in the solar system?",  # question 8
    "What is the capital of Australia?",  # question 9
    "Who is the current Prime Minister of Canada?",  # question 10
    "Who painted the Mona Lisa?",  # question 11
    "What is the currency of the European Union?",  # question 12
    "Who wrote the plays 'Hamlet' and 'Macbeth'?"  # question 13
]

answers = [
    "Paris",  # answer to question 1
    "Yen",  # answer to question 2
    "Joe Biden",  # answer to question 3
    "Rome",  # answer to question 4
    "Pacific Ocean",  # answer to question 5
    "Harper Lee",  # answer to question 6
    "Alexander Graham Bell",  # answer to question 7
    "Olympus Mons",  # answer to question 8
    "Canberra",  # answer to question 9
    "Justin Trudeau",  # answer to question 10
    "Leonardo da Vinci",  # answer to question 11
    "Euro",  # answer to question 12
    "William Shakespeare"  # answer to question 13
]

score = 0  # initialize score to 0

# ask each question and check the answer
for i in range(len(questions)):
    print(questions[i])
    response = input().lower()  # convert response to lowercase
    if response == answers[i].lower():  # compare lowercase response to lowercase answer
        print("Correct!")
        score += 1  # increment score by 1
    else:
        print("Incorrect. The correct answer is:", answers[i])

# print final score
print("Your final score is", score, "out of", len(questions))
