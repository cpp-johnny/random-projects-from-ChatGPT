import random

def generate_token():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

generate_token()
