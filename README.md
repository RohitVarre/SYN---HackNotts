## Scientific Programming in Python – submission 1

### Project title: Gesture-Customization-and-recognition

### Student name: Varre Rohit
  
#### Objective
The goal of this project is to detect real-time static hand signs using python and deploy it as a web application. A machine learning model is designed to detect live hand signs using the webcamera. These signs are usually static gestures or a part of sign language.

#### Tools and Frameworks
1. OpenCV - Image capturing and image recognition
2. Keras - Design and train the neural networks
3. Numpy, Pandas, os, Matplotlib, Seaborn - Data handling and visualization.

#### Inference from the web
There are similar words done previsouly on the sign recognition[1], but most of them relied on image processing and Convolutional Neural Network to predict the gesture. The major disadvantages with this approach are:
1. Image sensitivity to the background
2. High computational power
3. Sensitivity to the location of the hand
4. Possible lag between the image procuring and detection when deployed, due to higher computational time

#### How's this different
1. Google's mediapipe library[2] is an open source library that can be used to detect key coordinates of the human body parts like hands, face etc. The process of extracting the coordinates are highly optimized by the library and these coordinates can be processed and fed to an Artificial Neural Network. Instead of processing the image data from scratch and training a model to detect the hand, the hand coordinates which were efficiently extracted from mediapipe can be used to train the model. This way, we can reduce the computational time and power.
2. The differences in the hand sizes and the location of the hand from the camera can be tackled by taking the distance between the wrist point and various other hand coordinates as inputs. In this way, the location of the hand from the camera doesn't matter but instead, the relative position with respect to the wrist matters.
3. Standardizing these relative distances reduces other redundant factors like size of the hand and the distance between the hand and the camera.

#### Applications
This project has the potential to become an interface of communication for the deaf and dumb community with the normal world. The main challenges are:
1. To make the model robust so that it can be generalized to the live real world data.
2. To eliminate the lag between image capturing and prediction after deploying as a web application.

#### Working
##### Gesture Customization:
This set of code helps to customize static hand gestures, generate and save the data using OpenCV. The data comprises of the x and y coordinates of various key points on a palm. These coordinates are preprocessed and stored to train the model.

##### Gesture Model:
This is an Artificial Neural Network model that trains on the data which was generated during gesture customization. 

##### Gesture Prediction:
Live hand gestures are recognised through the webcam. The webcam captures the live coordinates of the hand and feeds it to the ANN model which recognises the handsigns. This can be deployed into a web or mobile application and data can be extracted from the mobile camera.

#### References:
[1] Sign language prediction - https://www.youtube.com/watch?v=pDXdlXlaCco  
[2] Mediapipe library - https://github.com/kinivi/hand-gesture-recognition-mediapipe

