# Obstacle Class 구현
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

class Obstacle:
    def __init__(self, x=350, y=600, width=700, height = 200):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.selected = False
    def move(self, mousex, mousey):
        if self.selected:
            self.x, self.y = mousex, mousey
    def click(self, mousex, mousey, clicked):
        if clicked and self.x-self.width/2 <= mousex <= self.x+self.width/2 and self.y - self.height/2 <= mousey <= self.y + self.height/2:
            self.selected = not self.selected
    def show(self):
        if self.selected:
            pygame.draw.rect(screen, RED, (self.x-self.width/2-5, self.y-self.height/2-5, self.width+10, self.height+10))
        pygame.draw.rect(screen, BLACK, (self.x-self.width/2, self.y-self.height/2, self.width, self.height))

obsarr = []
for i in range(3):
    obsarr.append(Obstacle())

def MoveAllObs(mousex, mousey, clicked):
    for i in range(3):
        obsarr[i].click(mousex, mousey, clicked)
        obsarr[i].move(mousex, mousey)
        obsarr[i].show()

while True:
    clicked = False
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            clicked = True
        if event.type == MOUSEMOTION:
            mousex, mousey = event.pos
    MoveAllObs(mousex, mousey, clicked)
    fpsClock.tick(FPS)
    pygame.display.flip()
