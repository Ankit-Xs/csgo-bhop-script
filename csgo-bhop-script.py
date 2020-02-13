#Made by Zen

import keyboard
import winsound
import time
          
def bhop():
    print("AutoBhop has launched")
    winsound.Beep(1000, 200)
    while True:
        if keyboard.is_pressed('space'):
            keyboard.press_and_release('space')
            time.sleep(0.09)
        else:
            continue

bhop()
        
            


        

