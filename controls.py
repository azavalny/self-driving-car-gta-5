import pydirectinput
import time

# Time between controls, can change
time_threshold = 0.09

#w
def forward():
    pydirectinput.keyDown("w")
    pydirectinput.keyUp("a")
    pydirectinput.keyUp("d")
    pydirectinput.keyUp("s")
#a
def turnLeft():
    pydirectinput.keyDown("a")
    pydirectinput.keyUp("w")
    pydirectinput.keyUp("d")
    pydirectinput.keyUp("s")
    time.sleep(time_threshold)
    pydirectinput.keyUp("a")
#d
def turnRight():
    pydirectinput.keyDown("d")
    pydirectinput.keyUp("a")
    pydirectinput.keyUp("w")
    pydirectinput.keyUp("s")
    time.sleep(time_threshold)
    pydirectinput.keyUp("d")
#s
def goBackward():
    pydirectinput.keyDown("s")
    pydirectinput.keyUp("a")
    pydirectinput.keyUp("w")
    pydirectinput.keyUp("d")
#wa
def turnLeftAndGoForward():
    pydirectinput.keyDown("w")
    pydirectinput.keyDown("a")
    pydirectinput.keyUp("a")
    pydirectinput.keyUp("s")
    time.sleep(time_threshold)
    pydirectinput.keyUp("a")
    pydirectinput.keyUp("w")
#wd
def turnRightAndGoForward():
    pydirectinput.keyDown("w")
    pydirectinput.keyDown("d")
    pydirectinput.keyUp("a")
    pydirectinput.keyUp("s")
    time.sleep(time_threshold)
    pydirectinput.keyUp("d")
    pydirectinput.keyUp("w")
#sa
def turnLeftAndGoBackward():
    pydirectinput.keyDown("s")
    pydirectinput.keyDown("a")
    pydirectinput.keyUp("a")
    pydirectinput.keyUp("s")
    time.sleep(time_threshold)
    pydirectinput.keyUp("a")
    pydirectinput.keyUp("s")

#sd
def turnRightAndGoBackward():
    pydirectinput.keyDown("s")
    pydirectinput.keyDown("d")
    pydirectinput.keyUp("a")
    pydirectinput.keyUp("s")
    time.sleep(time_threshold)
    pydirectinput.keyUp("d")
    pydirectinput.keyUp("s")

#no key
def releaseControls():
    pydirectinput.keyUp("a")
    pydirectinput.keyUp("w")
    pydirectinput.keyUp("d")
    pydirectinput.keyUp("s")

w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
wa =[0,0,0,0,1,0,0,0,0]
wd =[0,0,0,0,0,1,0,0,0]
sa =[0,0,0,0,0,0,1,0,0]
sd =[0,0,0,0,0,0,0,1,0]
nk =[0,0,0,0,0,0,0,0,1]
def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [W, S, A, D, WA, WD, SA, SD, NOKEY] boolean values.
    '''
    output = [0,0,0,0,0,0,0,0,0]

    if 'W' in keys and 'A' in keys:
        output = wa
    elif 'W' in keys and 'D' in keys:
        output = wd
    elif 'S' in keys and 'A' in keys:
        output = sa
    elif 'S' in keys and 'D' in keys:
        output = sd
    elif 'W' in keys:
        output = w
    elif 'S' in keys:
        output = s
    elif 'A' in keys:
        output = a
    elif 'D' in keys:
        output = d
    else:
        output = nk
    return output
def pauseKey():
    return "Y"

def output_to_key(vector):
    mapping = {
        0: 'w',
        1: 's',
        2: 'a',
        3: 'd',
        4: 'wa',
        5: 'wd',
        6: 'sa',
        7: 'sd',
        8: 'nk'
    }
    return mapping[argmax(vector)]