from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
import sys
sys.path.append('../Logic/Encrypt')
sys.path.append('../Logic/Steganography')
import RSA
import LSB
import base64

# Initialize the Flask application
app = Flask(__name__)

# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # do some fancy processing here....
    cv2.imwrite("1.PNG", img)
    
    print("-----Stegano Message Decrypt----"+"\n")
    messagetoDecrypt = LSB.Decode('1.PNG')
    messageRSADecrypt = RSA.decrypt_RSA(messagetoDecrypt)    
    print(messageRSADecrypt.decode())

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")

# start flask app
app.run(host="0.0.0.0", port=5000)