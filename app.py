#Import necessary libraries
from flask import Flask, render_template, Response, jsonify
import cv2
import tensorflow as tf
import os
import mediapipe as mp
import pandas as pd
import cv2
import numpy as np



#Initialize the Flask app
app = Flask(__name__)



## Intialize the model

code = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 
        8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 
        16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y'}
sign_char = ''

# Load the trained model
model = tf.keras.models.load_model('mediapipe.h5')

# Mediapipe methods to extract and display hand cooridnates
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.4,
    max_num_hands=1,
    min_tracking_confidence=0.4
)




cap = cv2.VideoCapture(0)

def gen_frames():
    global sign_char  
    while True:
        ret,frame = cap.read()
        image = cv2.flip(frame,1)
        x = []
        y = []
        z = []
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = True
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                for i in hand_landmarks.landmark:
                    x.append(i.x)
                    y.append(i.y)
                    z.append(i.z)                    
        
        
        if results.multi_hand_landmarks:
            df = pd.DataFrame({'x':x,'y':y,'z':z})
            data = np.array(df)
            data = data-data[0]                           # Same data scaling done during training
            data = data[1:]
            data = np.reshape(data,(-1,60))
            out = model.predict(data)
            output=np.argmax(out,axis=1)[0]
            sign_char = code[output]
            cv2.putText(image, code[output], (30,400), cv2.FONT_HERSHEY_TRIPLEX, 2.5, (127,127,255))
            
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
    message = {'greeting':sign_char}
    return jsonify(message)


if __name__ == "__main__":
    app.run()