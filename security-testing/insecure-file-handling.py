import os

def save_data(data):
    with open("data.txt", "w") as f:
        f.write(data)

data = "sensitive information"
save_data(data)
