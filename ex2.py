import sys 
import pygame as pg
from Library import *
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100,(255,0,0)) # สร้าง Object จากคลาส Button ขึ้นมา
Clock = pg.time.Clock()
while(run):
    eventlist =  pg.event.get()
    for event in eventlist:
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    screen.fill((255, 255, 255))
    btn.move_rect(eventlist)
    btn.draw(screen)
    pg.display.update()
    Clock.tick(60)