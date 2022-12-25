import random

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

generate_password()
