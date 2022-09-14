# 1, 2번 합친거 + object, obstacle 이동 상대적 좌표
import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("프로그래밍 실습")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MINT = (0, 255, 255)
RED = (255, 0, 0)

FPS = 200
fpsClock = pygame.time.Clock()

class Object:
    def __init__(self, x=25, y=25, vx=0, vy=0, ax=0, ay=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.clickmousex = 0
        self.clickmousey = 0
        self.firstplacex = self.x
        self.firstplacey = self.y
        self.selected = False
    def move(self, mouesx, mousey):
        if self.selected:
            self.x = self.firstplacex + mousex - self.clickmousex
            self.y = self.firstplacey + mousey - self.clickmousey
        else:
            if self.x + self.vx + self.ax <= 675 and self.y + self.vy + self.ay <= 675:
                self.x += self.vx
                self.vy += self.ay
                self.y += self.vy
    def click(self, mousex, mousey, clicked):
        if clicked and self.x-25 <= mousex <= self.x+25 and self.y-25 <= mousey <= self.y+25:
            self.selected = not self.selected
            self.firstplacex = self.x
            self.firstplacey = self.y
            self.clickmousex = mousex
            self.clickmousey = mousey
    def show(self):
        if self.selected:
            pygame.draw.ellipse(screen, MINT, (self.x-30, self.y-30, 60, 60), 0)
        pygame.draw.ellipse(screen, BLACK, (self.x-25, self.y-25, 50, 50), 0)

class Obstacle:
    def __init__(self, x=350, y=600, width=700, height = 200):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.selected = False
        self.clickmousex = 0
        self.clickmousey = 0
        self.firstplacex = self.x
        self.firstplacey = self.y
    def move(self, mousex, mousey):
        if self.selected:
            self.x = self.firstplacex + mousex - self.clickmousex
            self.y = self.firstplacey + mousey - self.clickmousey
    def click(self, mousex, mousey, clicked):
        if clicked and self.x-self.width/2 <= mousex <= self.x+self.width/2 and self.y - self.height/2 <= mousey <= self.y + self.height/2:
            self.selected = not self.selected
            self.firstplacex = self.x
            self.firstplacey = self.y
            self.clickmousex = mousex
            self.clickmousey = mousey
    def show(self):
        if self.selected:
            pygame.draw.rect(screen, RED, (self.x-self.width/2-5, self.y-self.height/2-5, self.width+10, self.height+10))
        pygame.draw.rect(screen, BLACK, (self.x-self.width/2, self.y-self.height/2, self.width, self.height))

objarr = []
for i in range(3):
    objarr.append(Object())

obsarr = []
for i in range(3):
    obsarr.append(Obstacle())

def MoveAllObj(mousex, mousey, clicked):
    for i in range(3):
        objarr[i].click(mousex, mousey, clicked)
        objarr[i].move(mousex, mousey)
        objarr[i].show()

def MoveAllObs(mousex, mousey, clicked):
    for i in range(3):
        obsarr[i].click(mousex, mousey, clicked)
        obsarr[i].move(mousex, mousey)
        obsarr[i].show()

while True:
    clicked = False
    screen.fill(WHITE)
    mousex, mousey = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            clicked = True
    MoveAllObj(mousex, mousey, clicked)
    MoveAllObs(mousex, mousey, clicked)
    fpsClock.tick(FPS)
    pygame.display.flip()
