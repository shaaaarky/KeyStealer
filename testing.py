import os

def CommitSuicide():    
    file_path = os.path.abspath(__file__) 
    os.remove(file_path)

path = "c:\\Users\\brads\\OneDrive\\Escritorio\\KeyStealer"
if __file__ == f"{path}\\{os.path.basename(__file__)}":
    print(True)  
else:
    CommitSuicide()
