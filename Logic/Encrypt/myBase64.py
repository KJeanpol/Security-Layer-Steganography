import base64


path='../Security/mykey.pem'

def stringToBase64(s):
    base64_bytes = s.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes

def base64ToString(b):
    base64_bytes = base64.b64encode(b)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def byteTobase64(b):
    return base64.b64encode(b)