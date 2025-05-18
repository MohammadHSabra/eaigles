# Hand Gesture Drawing API

This repository provides a simple Flask-based API for detecting hand gestures in images and enabling drawing functionality based on those gestures using **MediaPipe**.

---

## How It Works

- The API accepts an image in **base64** format via a POST request to the `/draw` endpoint.
- It processes the image using **MediaPipe Hands** to detect hand landmarks.
- Based on finger positions, it interprets gestures to:
  - **Draw** with one finger up
  - **Erase** with two fingers up
  - **Change color** with all five fingers up
  - **Pause drawing** with a closed fist
  - **Clear the canvas** with the thumb up
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
   ```

2. Create a virtual environment and activate it (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required libraries:

   ```bash
   pip install -r requirements.txt
   ```

   Or install dependencies manually:

   ```bash
   pip install flask flask-cors opencv-python mediapipe numpy
   ```

4. Run the Flask app:

   ```bash
   python app.py
   ```

   The server will start on port `8080` by default.

---

## Usage Example

Send a POST request to `/draw` with a JSON payload containing the base64 image string:

```json
{
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
}
```

The response will contain:

```json
{
  "result_image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
}
```

---

## Libraries Used

- **Flask** – Lightweight web framework for Python API.
- **Flask-CORS** – Enables Cross-Origin Resource Sharing for API requests.
- **OpenCV (cv2)** – Image processing and manipulation.
- **MediaPipe** – For hand landmark detection and gesture recognition.
- **NumPy** – Array manipulation.

---

## Important Notes

- The app maintains a global drawing canvas and state, so it is designed for continuous use per session.
- For multi-user or production environments, consider adding session management and thread safety.
- Base64-encoded images can be large; optimize client image size before sending.

---

## Stay Updated

Visit [eaigles.com](https://eaigles.com) – the visionary platform for more updates, innovations, and AI-powered tools.

---
