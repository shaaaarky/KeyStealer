import os
import string

# Iterate until it finds the usb drive and the 
path_test = r"Users\JohnBradshawCantos\Desktop\mremoveinst.txt"

def directory_searcher(path):
    drive_paths = []
    for char in string.ascii_uppercase:
        if os.path.exists(f"{char}:\\"):
            drive_paths.append(char)
        for letter in drive_paths:
            if os.path.exists(f"{letter}:\\{path}"):
                return f"Found file in {letter}"
                
x = directory_searcher(path=path_test)
print(x)