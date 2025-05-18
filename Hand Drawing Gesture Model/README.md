# Hand Gesture Drawing API

This repository provides a simple Flask-based API for detecting hand gestures in images and enabling drawing functionality based on those gestures using **MediaPipe**.

---

## How It Works

- The API accepts an image in **base64** format via a POST request to the `/draw` endpoint.
- It processes the image using **MediaPipe Hands** to detect hand landmarks.
- Based on finger positions, it interprets gestures to draw, erase, change color, pause, or clear the canvas.
- The processed image is returned as a base64-encoded JPEG to be displayed or further used.

---

## API Endpoints

- `GET /`  
  Returns a simple status message to verify that the service is running.

- `POST /draw`  
  Accepts JSON with a key `"image"` containing a base64-encoded image string.  
  Returns JSON with `"result_image"` containing the processed base64 image with drawings.

---

## Installation & Setup

1. Clone this repository:

   ```bash
   git clone <your-repo-url>
   cd <repo-folder>


Create a virtual environment and activate it (optional but recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate




Install required libraries:

pip install -r requirements.txt


Or install dependencies manually:

pip install flask flask-cors opencv-python mediapipe numpy


Run the Flask app:

python app.py


Usage Example
Send a POST request to /draw with a JSON payload containing the base64 image string:

{
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
}


The response will contain:

{
  "result_image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
}


Libraries Used
Flask – Lightweight web framework for Python API.

Flask-CORS – Enables Cross-Origin Resource Sharing for API requests.

OpenCV (cv2) – Image processing and manipulation.

MediaPipe – For hand landmark detection and gesture recognition.

NumPy – Array manipulation.





Important Notes
The app maintains a global drawing canvas and state, so it is designed for continuous use per session.

For multi-user or production environments, consider adding session management and thread safety.

Base64-encoded images can be large; optimize client image size before sending.



Stay Updated
Visit eaigles.com – the visionary platform for more updates, innovations, and AI-powered tools.







