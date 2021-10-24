from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64
import myBase64

path='Security/mykey.pem'

def encrypt_RSA(string):
    key = RSA.generate(2048)
    with open( path, 'wb' ) as f:
        f.write( key.exportKey( 'PEM' ))
    with open(path, 'r' ) as f:
        rsaKey = RSA.importKey( f.read() )  
    pkcs1CipherTmp = PKCS1_OAEP.new(rsaKey)
    encryptedString = pkcs1CipherTmp.encrypt(bytes(string, 'utf-8'))
    return encryptedString

def decrypt_RSA(encryptedString):
    encryptedString=myBase64.stringToBase64(encryptedString)
    with open(path, 'r' ) as f:
        rsaKey = RSA.importKey( f.read() )  
    pkcs1CipherTmp = PKCS1_OAEP.new(rsaKey)
    decryptedString = pkcs1CipherTmp.decrypt((encryptedString))
    return decryptedString