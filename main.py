import numpy as np
from PIL import ImageGrab
import time
import pydirectinput
import pygetwindow as gw
import sys
import tensorflow as tf
from tensorflow import keras
import tensorflow_hub as hub
import cv2

from controls import *
from get_keys import key_check

#python main.py driving=manual/self
if __name__ == "__main__":
    win = gw.getWindowsWithTitle("Grand Theft Auto V")[0]

    with tf.keras.utils.custom_object_scope({'KerasLayer': hub.KerasLayer}):
        model = tf.keras.models.load_model('model2.h5', custom_objects={'custom_lambda_function': lambda x: tf.tile(x, [1, 1, 1, 3])})
    print("model loaded")

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    #do autopilot driving
    paused = False
    while True:
        if not paused:
            x1, y1 = win.left, win.top
            x2, y2 = win.right, win.bottom
            screen = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (640, 480))
            #model predictions
            prediction = model.predict([screen.reshape(640, 480, 1)])
            control = np.argmax(prediction)
            print(prediction, control)

            if control == 0:
                forward()
            elif control == 1:
                goBackward()
            elif control == 2:
                turnLeft()
            elif control == 3:
                turnRight()
            elif control == 4:
                turnLeftAndGoForward()
            elif control == 5:
                turnRightAndGoForward()
            elif control == 6:
                turnLeftAndGoBackward()
            elif control == 7:
                turnRightAndGoBackward()
            else:
                releaseControls()
        
        keys = key_check()
        if pauseKey() in keys:
            if paused:
                paused=False
                print("Unpaused")
                time.sleep(1)
            else:
                print("Pausing")
                paused = True
                releaseControls()
                time.sleep(1)
        elif 'Q' in keys:
            break