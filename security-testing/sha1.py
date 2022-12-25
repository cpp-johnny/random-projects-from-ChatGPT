import hashlib

def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()

password = "mypassword"
hash_password(password)
