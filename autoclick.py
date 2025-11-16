# AutoClicker 
import pyautogui
import keyboard 
import time 
import threading
import winsound

# did set variables of time and clicks/second  | definir variaveis de tempo e clicks/seg
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

click_per_seg = 1000 # set quantity of seconds for click | definir quantidade de segundo por clicke
click_duration = None # duration | none = endless |

# variable of controll
clicando = False
parar = False 
contador = 0
start_time = 0

def autoclick():
    global clicando, parar, contador, start_time # pull the variables from outside the def | puxar as variáveis ​​externas de fora
    delay = 1.0 / click_per_seg # interval in clicker
    
    contador = 0 # counter
    start_time = time.time()
    
    print(f'auto clicker enable. ({click_per_seg} CPS)')
    winsound.Beep(1500, 80)
    
    while clicando and not parar:
        if click_duration and (time.time() - start_time >= click_duration):
            break 

        pyautogui.click()
        contador += 1
        time.sleep(delay)
   
    winsound.Beep(600, 200)
    print(f"\rClicks: {contador:,} | CPS: {contador/max(time.time()-start_time, 0.1):,.0f}", end="")
##

# start the auto clicker
def comecar():
    global clicando
    clicando = not clicando
    if clicando: 
        thread = threading.Thread(target=autoclick, daemon=True)
        thread.start()
    
    else:
        print('auto clicker paused in moment')


# shortcut | ATALHOS
keyboard.add_hotkey('ctrl+shift+space', comecar)
print("press CTRL+SHIFT+R for enable/disable the auto clicker")
print("press ESC for exit the program")

# end the program with 'esc' | finalizar programa com 'esc'
keyboard.wait('esc')
parar = True
print('program closed.')





















    

