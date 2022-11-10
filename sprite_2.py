import pygame as pg, sys
from pygame.locals import *
#this img 0,0-77,68
BLK = (0,0,0)
WHT = (255,255,255)
B = (0,0,255)

size = (1000,600)
width,height = size
screen = pg.display.set_mode(size)
screen.fill(BLK)
pg.display.update()

running = True
pg.init()
screen = pg.display.set_mode(size)
pg.display.set_caption('sprite')

#SSI means spirte sheet image
ssi = pg.image.load('fighter/Mr_Chou.png').convert_alpha()#member to have the pic in the file location and if its on a file fo "file_name"/"pic name"

def get_img(sheet,frame,width,height, scale, color):#this function makes it where u can get a single frame
    img = pg.Surface((width,height)).convert_alpha()#gets the wid anf hgt of the frame
    img.blit(sheet, (0,0), ((frame * width),0, width, height))#this set up frame
    #0,0 puts it in top left corner also gets rid of the black block
    img = pg.transform.scale(img, (width * scale, height * scale))# this is what set the scale function
    img.set_colorkey(color)#if u use this make sure to declre it
    
    return img#returns the function
    #like screen img is a surface and i can blit on it

frame_0 = get_img(ssi,0,77,68,1,B)#this singles out a frame 
frame_1 = get_img(ssi,1,77,68,1,B) 
frame_2 = get_img(ssi,2,77,68,1,B) 
frame_3 = get_img(ssi,3,77,68,1,B) 
frame_4 = get_img(ssi,4,77,68,1,B) 

while running:

    #when u make a background make all new screen updates after it
    screen.fill(WHT)

    #display img
    screen.blit(frame_0,(0,0))
    screen.blit(frame_1,(77,0))
    screen.blit(frame_2,(231,0))
    screen.blit(frame_3,(308,0))
    screen.blit(frame_4,(385,0))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.update()

pg.quit()
