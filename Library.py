import pygame as pg
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,colour=(0,0,0)):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.colour = colour
        self.default_colour = colour
    def draw(self,screen):
        pg.draw.rect(screen,self.colour,(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0,colour = (0,0,0)):
        Rectangle.__init__(self, x, y, w, h,colour)
    
    def isMouseOn(self):
        mx,my = pg.mouse.get_pos()
        if (mx >= self.x and mx <= self.x + self.w) and (my >= self.y and my <= self.y + self.h):
            return True
        return False
    
    def isMouseOnPress(self):
        ms = pg.mouse.get_pressed()
        return ms[0]
    
    def change_colour(self):
        if self.isMouseOn():
            self.colour = (100,100,100)
            if self.isMouseOnPress():
                self.colour = (120,20,220)
        else:
            self.colour = self.default_colour

    def move_rect(self,eventList):
        for event in eventList:
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    self.x += 100  
                elif event.key == pg.K_a:
                    self.x -= 100
                elif event.key == pg.K_w:
                    self.y -= 100 
                elif event.key == pg.K_s:
                    self.y += 100
class InputBox:
    def __init__(self, x, y, w, h, text='',colour=(0,0,0)):
        self.rect = pg.Rect(x, y, w, h)
        self.color = colour
        self.after_color = (100,100,100)
        self.text = text
        self.font = pg.font.Font('freesansbold.ttf', 32)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color if self.active else self.color # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
    def clear(self, Screen):
        self.text = ''
        self.txt_surface = self.font.render(self.text, True, self.color)
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(Screen, self.color, self.rect, 2)

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
    def ret(self):
        if self.isMouseOn():
            self.colour = (120,20,220)
            if self.isMouseOnPress():
                self.clear()
                return self.text
        else:
            self.color = self.defual_colour
class InputBoxDigit:
    def __init__(self, x, y, w, h, text='',colour=(0,0,0)):
        self.rect = pg.Rect(x, y, w, h)
        self.color = colour
        self.after_color = (100,100,100)
        self.defual_colour = self.color
        self.text = text
        self.font = pg.font.Font('freesansbold.ttf', 32)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color if self.active else self.color # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode.isdigit():
                        self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
    def clear(self, Screen):
        self.text = ''
        self.txt_surface = self.font.render(self.text, True, self.color)
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
    def ret(self):
        if self.isMouseOn():
            self.colour = (120,20,220)
            if self.isMouseOnPress():
                self.clear()
                return self.text
        else:
            self.color = self.defual_colour
class ButtonCheck(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0,colour = (0,0,0)):
        Rectangle.__init__(self, x, y, w, h,colour)
    
    def isMouseOn(self):
        mx,my = pg.mouse.get_pos()
        if (mx >= self.x and mx <= self.x + self.w) and (my >= self.y and my <= self.y + self.h):
            return True
        return False
    
    def isMouseOnPress(self):
        ms = pg.mouse.get_pressed()
        return ms[0]
    
    def change_colour(self):
        if self.isMouseOn():
            self.colour = (100,100,100)
            if self.isMouseOnPress():
                self.colour = (120,20,220)
                # print(self.text)
                # self.text = ''
        else:
            self.colour = self.default_colour

    def move_rect(self,eventList):
        for event in eventList:
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    self.x += 100  
                elif event.key == pg.K_a:
                    self.x -= 100
                elif event.key == pg.K_w:
                    self.y -= 100 
                elif event.key == pg.K_s:
                    self.y += 100
