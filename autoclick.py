# AutoClicker 
import pyautogui
import keyboard 
import time 
import threading
import winsound

# definir fariaveis de tempo e clicks/seg
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

click_per_seg = 1000 # definir quantidade de segundo por clicke
click_duration = None # duração | none = infinito |

# variaveis de controle 
clicando = False
parar = False 
contador = 0
start_time = 0

def autoclick():
    global clicando, parar, contador, start_time
    delay = 1.0 / click_per_seg # intervalo entre click
    
    contador = 0
    start_time = time.time()
    
    print(f'autoclicker ativado. ({click_per_seg} CPS)')
    winsound.Beep(1500, 80)
    
    while clicando and not parar:
        if click_duration and (time.time() - start_time >= click_duration):
            break 

        pyautogui.click()
        contador += 1
        time.sleep(delay)
   
    winsound.Beep(600, 200)
    print(f"\rCliques: {contador:,} | CPS: {contador/max(time.time()-start_time, 0.1):,.0f}", end="")
##

def começar():
    global clicando
    clicando = not clicando
    if clicando: 
        thread = threading.Thread(target=autoclick, daemon=True)
        thread.start()
    
    else:
        print('autoclicker pausado no momento')


# ATALHOS
keyboard.add_hotkey('ctrl+shift+space', começar)
print("Pressione CTRL+SHIFT+R para ativar/desativar o autoclicker")
print("Pressione ESC para sair do programa")

# finalizar programa com 'esc'
keyboard.wait('esc')
parar = True
print('programa encerrado.')





















    