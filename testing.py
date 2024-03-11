import os
p = "c:\\Users\\brads\\OneDrive\\Escritorio\\KeyStealer"

def file_in_dir(path):
    current_script = os.path.basename(__file__)
    return os.path.exists(f"{path}\\{current_script}")

print(file_in_dir(p))
