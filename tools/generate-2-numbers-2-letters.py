import random

for i in range(100):
    def generate_string():
        number1 = str(random.randint(0, 9))
        number2 = str(random.randint(0, 9))
        letter1 = random.choice('abcdefghijklmnopqrstuvwxyz')
        letter2 = random.choice('abcdefghijklmnopqrstuvwxyz')
        return number1 + number2 + letter1 + letter2
    
    result = generate_string()
    print(result)
