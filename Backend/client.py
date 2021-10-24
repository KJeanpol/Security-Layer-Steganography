from __future__ import print_function
import requests
import json
import cv2
import sys
sys.path.append('../Logic/Encrypt')
sys.path.append('../Logic/GA')
sys.path.append('../Logic/Steganography')
import RSA
import GA
import LSB


addr = 'http://localhost:5000'
test_url = addr + '/api/test'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

print("-----Creating new Image----"+"\n")
GA.GA('../Data/fruit.jpg',500000)

print("-----Encripting Message----"+"\n")
messageRSA = RSA.encrypt_RSA("Esto es una prueba 2")

print("---- Executing Steganography Message----"+"\n")
LSB.Stego_Encrypt('../Data/solution_25000.png',messageRSA,'../Data/carro70.PNG')

img = cv2.imread('../Data/carro70.PNG')
# encode image as jpeg
_, img_encoded = cv2.imencode('.PNG', img)
# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tobytes(), headers=headers)
print(json.loads(response.text))