import base64

def decode(data):
    return base64.b64decode(data)

data = "c2VjcmV0"
decode(data)
