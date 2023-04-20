import sys
import pygame as pg
from Library import *
pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
font = pg.font.Font('freesansbold.ttf', 32)
btn = ButtonCheck(500,200,100,100,(255,0,0))
defual_color = btn.colour
input_box1 = InputBox(100, 100, 140, 32,colour=(200,100,100)) # สร้าง InputBox1
input_box2 = InputBox(100, 200, 140, 32,colour=(100,200,100)) # สร้าง InputBox2
input_box3 = InputBoxDigit(100, 300, 140, 32,colour=(100,100,200)) 
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True
Clock = pg.time.Clock()
# mes = "Name : " + input_box1.text + " Last Name : " + input_box2.text + " Age : " + input_box3.text
subtitle = font.render('Program Test',True,(0,0,0))
subtitle_rect = subtitle.get_rect()
subtitle_rect.center = (400,50)

subbut = font.render('Submit!',True,(0,0,0))
subbut_rect = subbut.get_rect()
subbut_rect.center = (550,160)
while run:
    screen.fill((255, 255, 255))
    screen.blit(subtitle,subtitle_rect)
    screen.blit(subbut,subbut_rect)
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    btn.draw(screen)
    if btn.isMouseOn():
        btn.colour = (120,20,220)
        if btn.isMouseOnPress():
            mes = "Name : " + input_box1.text + " Last Name : " + input_box2.text + " Age : " + input_box3.text
            sub = font.render(mes,True,(0,0,0))
            sub_rect = sub.get_rect()
            sub_rect.center = (400,400)
            print(mes)
            screen.blit(sub,sub_rect)
            input_box1.clear(screen)
            input_box2.clear(screen)
            input_box3.clear(screen)
    else:
        btn.colour = defual_color
    for box in input_boxes:
        box.update()
        box.draw(screen)
        # box.clear(screen)
    # pg.time.delay(1)
    Clock.tick(5)
    pg.display.update()
    