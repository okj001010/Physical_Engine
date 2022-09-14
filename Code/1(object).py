# Object Class 구현
import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("프로그래밍 실습")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

FPS = 100
fpsClock = pygame.time.Clock()

class Object:
    def __init__(self, x=25, y=25, vx=0.1, vy=0, ax=0, ay=0.1):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.selected = False
    def move(self, mouesx, mousey):
        if self.selected:
            self.x, self.y = mousex, mousey
        else:
            if self.x + self.vx + self.ax <= 675 and self.y + self.vy + self.ay <= 675:
                self.x += self.vx
                self.vy += self.ay
                self.y += self.vy
    def click(self, mousex, mousey, clicked):
        if clicked and self.x-25 <= mousex <= self.x+25 and self.y-25 <= mousey <= self.y+25:
            self.selected = not self.selected
    def show(self):
        if self.selected:
            pygame.draw.ellipse(screen, RED, (self.x-30, self.y-30, 60, 60), 0)
        pygame.draw.ellipse(screen, BLACK, (self.x-25, self.y-25, 50, 50), 0)

objarr = []
for i in range(3):
    objarr.append(Object())

def MoveAllObj(mousex, mousey, clicked):
    for i in range(3):
        objarr[i].click(mousex, mousey, clicked)
        objarr[i].move(mousex, mousey)
        objarr[i].show()

while True:
    clicked = False
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            clicked = True
            mousex, mousey = event.pos
        if event.type == MOUSEMOTION:
            mousex, mousey = event.pos
    MoveAllObj(mousex, mousey, clicked)
    fpsClock.tick(FPS)
    pygame.display.flip()
