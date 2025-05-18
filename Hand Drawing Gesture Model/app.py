from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64
from utils import process_frame  # Assuming your hand gesture code is in `utils.py`
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and all domains


def readb64(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def encode_image(img):
    _, buffer = cv2.imencode('.jpg', img)
    b64 = base64.b64encode(buffer).decode('utf-8')
    return f"data:image/jpeg;base64,{b64}"

@app.route('/')
def health():
    return 'Service is running', 200


@app.route('/draw', methods=['POST'])
def draw():
    data = request.json
    if 'image' not in data:
        return jsonify({'error': 'Missing image field'}), 400

    # Convert the base64 image into a numpy array (OpenCV image)
    frame = readb64(data['image'])

    # Process the frame using your existing hand gesture detection code
    result = process_frame(frame)

    # Encode the result image back to base64
    encoded_result = encode_image(result)

    return jsonify({'result_image': encoded_result})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
