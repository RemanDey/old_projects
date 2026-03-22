# app.py
import base64
import cv2
import numpy as np
from io import BytesIO
from PIL import Image
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'replace-with-a-secret'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# Simple index page serving the client HTML
@app.route('/')
def index():
    return render_template('index.html')

# Called when client sends a frame (base64 jpeg)
@socketio.on('frame')
def handle_frame(data):
    # data is a dict { 'b64': 'data:image/jpeg;base64,...' }
    b64 = data.get('b64', None)
    if not b64:
        return

    # Remove prefix if present
    if b64.startswith('data:image'):
        b64 = b64.split(',', 1)[1]

    try:
        jpg_bytes = base64.b64decode(b64)
        # Use PIL to open then convert to ndarray (RGB)
        img = Image.open(BytesIO(jpg_bytes)).convert('RGB')
        arr = np.array(img)  # shape (h, w, 3), RGB
        # Convert RGB -> BGR for OpenCV
        frame = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)

        # Display using OpenCV
        cv2.imshow('Visitor Camera', frame)
        # waitKey required to refresh window. Use 1 ms to be non-blocking.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Optionally allow closing the window with 'q'
            socketio.stop()
    except Exception as e:
        print("Error decoding frame:", e)

if __name__ == '__main__':
    print("Open http://<server_ip>:5000/ in the visitor's browser (or localhost)")
    socketio.run(app, host='0.0.0.0', port=5000)
