#Import necessary libraries
from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np



#Initialize the Flask app
app = Flask(__name__)

cap = cv2.VideoCapture(0)

def gen_frames():  
    while True:
        ret,frame = cap.read()
        image = frame
        ret, buffer = cv2.imencode('.jpg', image)
        image = buffer.tobytes()
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')
            

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/sign')
def sign():
    message = {'greeting':'Hello from Flask!'}
    return jsonify(message)


if __name__ == "__main__":
    app.run()