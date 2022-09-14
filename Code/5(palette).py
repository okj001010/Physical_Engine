# 가장 위에 있는거만 움직이게 만들기
import pygame, sys, random
from pygame.locals import *

pygame.init()
SCREENWIDTH = 1200
SCREENHEIGHT = 700
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("프로그래밍 실습")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MINT = (0, 255, 255)
RED = (255, 0, 0)

LEFT= 1

FPS = 200
fpsClock = pygame.time.Clock()

class Object: # 물체 class
    def __init__(self, x=25, y=25, vx=0, vy=0, ax=0, ay=0): # 초기화 과정 (tkinter로 할 계획)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
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
    def move(self, mouesx, mousey): # 물체 이동 함수
        if self.selected: # 클릭되어 있으면
            self.x = self.firstplacex + mousex - self.clickmousex # 클릭한 점을 중심으로 상대적으로 이동
            self.y = self.firstplacey + mousey - self.clickmousey
        else: # 클릭된 상태가 아니라면
            if self.x + self.vx + self.ax <= 675 and self.y + self.vy + self.ay <= 675: # 화면 안에 있을 때까지만 이동
                self.x += self.vx
                self.vy += self.ay
                self.y += self.vy
    def click(self, mousex, mousey, clicked):
        if clicked and self.x-25 <= mousex <= self.x+25 and self.y-25 <= mousey <= self.y+25: # 물체 좌표 안에 마우스 좌표가 있으면 True 반환
            return True
    def show(self): 
        if self.selected:
            pygame.draw.ellipse(screen, MINT, (self.x-30, self.y-30, 60, 60), 0) # 클릭된 경우 테두리 출력
        pygame.draw.ellipse(screen, self.color, (self.x-25, self.y-25, 50, 50), 0) # 물체 출력

class Obstacle: # 장애물? class
    def __init__(self, x=600, y=600, width=SCREENWIDTH, height = 200): # 초기화 과정 (tkinter로 할 계획)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.clickmousex = 0
        self.clickmousey = 0
        self.firstplacex = self.x
        self.firstplacey = self.y
        self.selected = False
    def move(self, mousex, mousey): # 장애물 이동 함수
        if self.selected: # 클릭되어 있으면
            self.x = self.firstplacex + mousex - self.clickmousex # 클릭한 점을 중심으로 상대적으로 이동
            self.y = self.firstplacey + mousey - self.clickmousey
    def click(self, mousex, mousey, clicked):
        if clicked and self.x-self.width/2 <= mousex <= self.x+self.width/2 and self.y - self.height/2 <= mousey <= self.y + self.height/2: # 장애물 좌표 안에 마우스 좌표가 있으면 True 반환
            return True
    def show(self):
        if self.selected:
            pygame.draw.rect(screen, RED, (self.x-self.width/2-5, self.y-self.height/2-5, self.width+10, self.height+10)) # 클릭된 경우 테두리 출력
        pygame.draw.rect(screen, self.color, (self.x-self.width/2, self.y-self.height/2, self.width, self.height)) # 장애물 출력

class Palette: # 팔레트 class
    def show(self): # 팔레트 출력
        pygame.draw.rect(screen, BLACK, (0, 0, SCREENWIDTH, 100))
        pygame.draw.circle(screen, WHITE, (300, 50), 30)
        pygame.draw.rect(screen, WHITE, (500, 20, 100, 60))
    def clicked(self, mousex, mousey, clicked):
        if clicked: # 클릭되었는데
            if ((mousex-300)**2+(mousey-50)**2)**0.5 < 30: # circle 안에 클릭했으면
                objarr.append(Object()) # 물체 append
            if 500 < mousex < 600 and 20 < mousey < 80: # rectangle 안에 클릭했으면
                obsarr.append(Obstacle()) # 장애물 append

objarr = []
obsarr = []
objorder = []
palette = Palette()

def MoveAllObj(mousex, mousey, clicked):
    anyselected = False
    for i in range(len(objarr)): # 클릭된게 하나라도 있는지 확인
        # 한번에 여러개 클릭 못하게 하려고 하는 작업
        if objarr[i].selected:
            anyselected = True
            break
    if anyselected: # 클릭된게 하나라도 있을 경우
        if objarr[i].click(mousex, mousey, clicked):
            objarr[i].selected = not objarr[i].selected
            #objarr[i].firstplacex, objarr[i].firstplacey = objarr[i].x, objarr[i].y
            #objarr[i].clickmousex, objarr[i].clickmousey = mousex, mousey
    if not anyselected: # 클릭된게 하나도 없었던 상황에서
        for i in range(len(objarr)):
            if objarr[i].click(mousex, mousey, clicked): # 클릭되면
                objarr[i].selected = not objarr[i].selected # 선택함
                objarr[i].firstplacex, objarr[i].firstplacey = objarr[i].x, objarr[i].y # 상대적 좌표로 움직이게 하려고 하는 작업
                objarr[i].clickmousex, objarr[i].clickmousey = mousex, mousey # 상대적 좌표로 움직이게 하려고 하는 작업
                break
    for i in range(len(objarr)-1, -1, -1): # 순서대로 이동시키고 출력
        objarr[i].move(mousex, mousey)
        objarr[i].show()

def MoveAllObs(mousex, mousey, clicked): # MoveAllObj와 거의 동일함
    anyselected = False
    for i in range(len(obsarr)):
        if obsarr[i].selected:
            anyselected = True
            break
    if anyselected:
        if obsarr[i].click(mousex, mousey, clicked):
            obsarr[i].selected = not obsarr[i].selected
            obsarr[i].firstplacex, obsarr[i].firstplacey = obsarr[i].x, obsarr[i].y
            obsarr[i].clickmousex, obsarr[i].clickmousey = mousex, mousey
    if not anyselected:
        for i in range(len(obsarr)):
            if obsarr[i].click(mousex, mousey, clicked):
                obsarr[i].selected = not obsarr[i].selected
                obsarr[i].firstplacex, obsarr[i].firstplacey = obsarr[i].x, obsarr[i].y
                obsarr[i].clickmousex, obsarr[i].clickmousey = mousex, mousey
                break
    for i in range(len(obsarr)-1, -1, -1):
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
        if event.type == MOUSEBUTTONDOWN and event.button == LEFT: # 왼쪽 버튼 클릭되면
            clicked = True # clicked True
    palette.show() # palette 보여주고
    palette.clicked(mousex, mousey, clicked) # 팔레트 클릭되었는지 확인하고
    MoveAllObj(mousex, mousey, clicked) # 물체 다 움직이고
    MoveAllObs(mousex, mousey, clicked) # 장애물 다 움직임
    fpsClock.tick(FPS)
    pygame.display.flip()
