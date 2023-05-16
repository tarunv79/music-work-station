import winsound
import time
import threading
import keyboard
from pynput.keyboard import Key, Listener

flag = 1
inp = 'x'
keyInputVal = ''

############## K E Y B O A R D   E V E N T S ###########################
def on_press(key):
    print('{0} pressed'.format(
        key))
    keyInputVal = key
    print(keyInputVal)

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


#######################################################################
def playSound1():
    while inp is not 'z':
        if inp is 'a':
           # inp = 'x'
            winsound.PlaySound('sound1.wav',winsound.SND_FILENAME)

def playSound2():
    while inp is not 'z':
        if inp is 's':
           # inp = 'x'
            winsound.PlaySound('sound2.wav',winsound.SND_FILENAME)

def playSound3():
    while inp is not 'z':
        if inp is 'd':
            #inp = 'x'
            winsound.PlaySound('sound3.wav',winsound.SND_FILENAME)

def playSound4():
    while inp is not 'z':
        if inp is 'f':
            #inp = 'x'
            winsound.PlaySound('sound4.wav',winsound.SND_FILENAME)

class myThread(threading.Thread):
    def __init__(self,param):
        threading.Thread.__init__(self)
        self.param= param
    def run(self):
        if self.param is 1:
            playSound1()
        if self.param is 2:
            playSound2()
        if self.param is 3:
            playSound3()
        if self.param is 4:
            playSound4()
        
print("initializing")
while flag:
    try:
        if keyInputVal == '0':
            print("exiting from the program")
            flag = 0

    except:
        print("Error occured!")
    
