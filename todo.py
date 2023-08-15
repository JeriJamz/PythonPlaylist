import time,sys, pyautogui as pag
#this is the logic
#this is now an app
global nput

def sprint(z): #the slow print
    for y in z:
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(.05)

#make a list that will hold 1 - 64

class ToDo:
    def __init__(self, TodoList):
        self.TodoList
        self.click
        self.clickNdrag
        self.UiFunc
        self.Commands

    def TodoList():#idk kno if this is vaild yet
        newItem = input()#working on a print and idk if this takes the strings or just the numbers yet
        nput = input()#dont think i need this
        tDlist = list(range(str(int(x,64))))#this gone give me hell
        for x in range(tDlist(newItem)):#this is the algo to store the item for the day. Max is 64 for the day
            x + 1

    def Click():#from here down are "features ima add"
        pass

    def clickNdrag():
        pass

    def UiFunc():
        pass

    def Commands():
        pass
    
sprint('return 0\n')
tr = True

nput = input()

while nput.lower() == "yes":
    while tr:
        f'<Exit>' == sys.exit  
        print("Todo Listing")
        nput = input()
        print(f'{nput}')
        
    

