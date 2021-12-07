import cv2 
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model


cap = cv2.VideoCapture(0)
while True:

    _, frame = cap.read()
    x , y, c = frame.shape
    frame = cv2.flip(frame, 1)
    cv2.imshow("Output", frame)
    
    
    
    
    
    
    
    
    
    
    
    
    if cv2.waitKey(1) == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()