import pyautogui as pag
import time, sys

def delay_print(c):
    for s in c:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(.005)

def delay_print2(c):
    for s in c:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(.05)

delay_print("Little automation trick. it keeps the mouse active\n")

Width,Height = pag.size()
Width,Height = (1200,800)


while True:
    pag.moveRel(0,10)#down
    time.sleep(1)
    pag.moveRel(10,0)#right
    time.sleep(1)
    pag.moveRel(10,10)#diaginal
    time.sleep(1)
    pag.moveRel(0,0)#no movement
    time.sleep(1)
    delay_print2("****Warning |AUTO-CLICK-ALERT|*****\n")
    pag.click(100,20)
    time.sleep(1)
    break
    
