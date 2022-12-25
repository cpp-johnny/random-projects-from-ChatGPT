import getpass

def create_account(username, password):
    with open("credentials.txt", "a") as f:
        f.write(f"{username},{password}\n")

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
create_account(username, password)
