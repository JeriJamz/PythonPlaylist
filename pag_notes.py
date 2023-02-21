import pyautogui as pag, time, sys

def lp(a):
    for i in aL:
        sys.stdout.write(aL)
        sys.stdout.flush()
        time.sleep(1.5)

pag.PAUSE = 1#this till pause it
pag.FAILSAFE = True #this is the fail safe feature


#top left(orgin), bottem right(maxout(1080,1080))
#the TV is 1360 X 768
#need to find yours. look it up in your search tab or you can look into your monitor specs
print(pag.size())#this will print the size but you can set it also, jmp, ln 10
width,height = pag.size()#this gives a reponsive feature i think

#this will go over moving the mouse
for i in range(10):
    pag.moveTo(686,152, duration=.25)#moveTo moves the mouse to coorainates
    pag.moveTo(620,768, duration=.25)
    pag.moveTo(765,845, duration=.25)
    pag.moveTo(485,1360, duration=.25)
    pag.moveTo(0,0, duration=.25)

lp("\n L O A D I N ...\n")

for l in range(10):
    pag.moveRel(-100,0, duration=.25)#moveRel Moves the cursor buts its relative to the position
    pag.moveRel(100,100, duration=.25)
    pag.moveRel(0,0, duration=.25)
    pag.moveRel(0,100, duration=.25)








