import numpy as np
import os
from controls import *
from get_keys import key_check
import cv2
import pygetwindow as gw
from PIL import ImageGrab


file_name = 'data/train2.npy'
if os.path.isfile(file_name):
    print("File exists, loading previous training data")
    training_data = np.load(file_name, allow_pickle=True).tolist()
else:
    print("File does not exist, creating new training data")
    training_data = []

def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    win = gw.getWindowsWithTitle("Grand Theft Auto V")[0]
    paused=False
    print("Collecting New Training Data")
    while True:
        if not paused:
            x1, y1 = win.left, win.top
            x2, y2 = win.right, win.bottom
            screen = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (640, 480))
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen, output])

            if len(training_data) %1000 == 0:
                print(len(training_data))
                np.save(file_name, np.array(training_data, dtype=object))
            
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

main()