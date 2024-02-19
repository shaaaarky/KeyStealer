import os

def grep(file, directory):
    for item in os.listdir(directory):
        if item == file:
            print(f"[/] {item}")
        else:
            print("[/] ERROR: No file name matching input" )

