#let see if I can get me computer to open google
import pyautogui as pag, webbrowser


webbrowser.open_new('chrome')#this just open chrome 
webbrowser.open_new_tab('www.google.com')#but this is gonna pull up google on the default


pag.moveTo(400,500,5)
pag.moveTo(600,5,2)
pag.click()
pag.moveTo(600,270,2)
pag.click()
pag.write('This works')
pag.moveTo(800,270,1)
pag.press('enter')


print(pag.size())#get screen size

