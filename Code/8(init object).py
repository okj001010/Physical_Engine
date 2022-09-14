# 가장 위에 있는거만 움직이게 만들기
import pygame, sys, random
from pygame.locals import *
from tkinter import *

pygame.init()
SCREENWIDTH = 1200
SCREENHEIGHT = 700
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("프로그래밍 실습")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MINT = (0, 255, 255)
RED = (255, 0, 0)

LEFT= 1 # mouse button event 처리할 때 필요한 상수
RIGHT = 3

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
    def click(self, mousex, mousey, clicked, r_clicked):
        if self.x-25 <= mousex <= self.x+25 and self.y-25 <= mousey <= self.y+25: # 물체 좌표 안에 마우스 좌표가 있으면 True 반환
            if clicked or r_clicked:
                return True
    def initevery(self, n):
        window = Tk()
        window.title("물체 "+str(n))
        l = [0 for i in range(6)] #레이블 변수 초기화
        b = [0 for i in range(6)] #버튼 변수 초기화
        e = [0 for i in range(6)] #엔트리 변수 초기화
        toentry = ["초기 x좌표", "초기 y좌표", "초기 x속도", "초기 y속도", "초기 x가속도", "초기 y가속도"] #받은 변수 설정

        def buttondown1():#첫번째의 입력값을 받았을 때
            self.x = float(e[0].get()) # e[0]에서 입력받은 값을 check변수에 넣는다(e를 직접적으로 사용이 불가능하므로)
            e[0].delete(0, END) #원래 있던 값(입력 받은 숫자)를 지운다.
            e[0].insert(0, "는 "+str(self.x)+"m 입니다") #문자열로 입력받은 값을 출력하여 보여준다.

        def buttondown2():
            self.y = SCREENHEIGHT - float(e[1].get()) # float대신 eval도 가능
            e[1].delete(0, END)
            e[1].insert(0, "는 "+str(SCREENHEIGHT-self.y)+"m 입니다")
                
        def buttondown3():
            self.vx = float(e[2].get()) # float대신 eval도 가능
            e[2].delete(0, END)
            e[2].insert(0, "는 "+str(self.vx)+"m/s 입니다.")
                
        def buttondown4():
            self.vy = -float(e[3].get()) # float대신 eval도 가능
            e[3].delete(0, END)
            e[3].insert(0, "는 "+str(-self.vy)+"m/s 입니다.")
                
        def buttondown5():
            self.ax = float(e[4].get()) # float대신 eval도 가능
            e[4].delete(0, END)
            e[4].insert(0, "는 "+str(self.ax)+"m/s^2 입니다.")
                
        def buttondown6():
            self.ay = -float(e[5].get()) # float대신 eval도 가능
            e[5].delete(0, END)
            e[5].insert(0, "는 "+str(-self.ay)+"m/s^2 입니다.")

        def initquit():
            window.destroy()
        info = [0, 0, 0]
        info[0] = Label(window, text = "현재 좌표(m): ("+str(self.x)+", "+str(SCREENHEIGHT-self.y)+")")
        info[1] = Label(window, text = "현재 속도(m/s): ("+str(self.vx)+", "+str(-self.vy)+")")
        info[2] = Label(window, text = "현재 가속도(m/s^2): ("+str(self.ax)+", "+str(-self.ay)+")")
        for i in range(3):
            info[i].grid(row=i, columnspan=3)
        for i in range(6): #6개의 선택지를 만들므로
            l[i] = Label(window, text = toentry[i]).grid(row=i+3, column=0) #레이블을 toentry문자열을 넣어 만들고 위치시킨다.
            e[i] = Entry(window) #e는 입력받게 만든다.
            e[i].grid(row=i+3, column=1) #grid를 같이 초기화 하지 않는 이유는 같이 하면 입력받은 값 뿐만 아니라 다른 정보도 입력되어 데이터만 골라낼 수 없으므로
            if i == 0:
                b[i] = Button(window, text="입력", command = buttondown1).grid(row=i+3,column=2) #입력받았을 경우에 entry에 있는 값을 받는 함수로 이동하는 과정으로 이 방법을 사용하지 않으면 buttondown1에서 entry값을 문자로 변환시킨 후에 for문을 돌면서 다시 숫자로 받는 과정에서 오류가 발생한다.
            elif i == 1:
                b[i] = Button(window, text="입력", command = buttondown2).grid(row=i+3,column=2)
            elif i == 2:
                b[i] = Button(window, text="입력", command = buttondown3).grid(row=i+3,column=2)
            elif i == 3:
                b[i] = Button(window, text="입력", command = buttondown4).grid(row=i+3,column=2)
            elif i == 4:
                b[i] = Button(window, text="입력", command = buttondown5).grid(row=i+3,column=2)
            elif i == 5:
                b[i] = Button(window, text="입력", command = buttondown6).grid(row=i+3,column=2)
        quitbutton = Button(window, text="종료", command = initquit).grid(row = 9, columnspan = 3)
        window.mainloop()

    def show(self): 
        if self.selected:
            pygame.draw.ellipse(screen, MINT, (self.x-30, self.y-30, 60, 60), 0) # 클릭된 경우 테두리 출력
        pygame.draw.ellipse(screen, self.color, (self.x-25, self.y-25, 50, 50), 0) # 물체 출력

class Obstacle: # 장애물? class
    def __init__(self, x=600, y=600, width=SCREENWIDTH, height = 200): # 초기화 과정 (tkinter로 할 계획)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # 색깔 랜덤 적용
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.clickmousex = 0
        self.clickmousey = 0
        self.firstplacex = self.x
        self.firstplacey = self.y
        self.firstwidth = self.width
        self.firstheight = self.height
        self.selected = False
        self.r_selected = False
        self.place = [False, False, False, False]
    def move(self, mousex, mousey): # 장애물 이동 함수
        if self.selected: # 클릭되어 있으면
            self.x = self.firstplacex + mousex - self.clickmousex # 클릭한 점을 중심으로 상대적으로 이동
            self.y = self.firstplacey + mousey - self.clickmousey
        if self.r_selected:
            self.x = self.firstplacex + (mousex - self.clickmousex)/2
            self.y = self.firstplacey + (mousey - self.clickmousey)/2
            if self.place[0]: # 오른쪽 위 클릭된 경우
                self.width = self.firstwidth + (mousex - self.clickmousex)
                self.height = self.firstheight - (mousey - self.clickmousey)
            if self.place[1]: # 오른쪽 아래 클릭된 경우
                self.width = self.firstwidth + (mousex - self.clickmousex)
                self.height = self.firstheight + (mousey - self.clickmousey)
            if self.place[2]: # 왼쪽 아래 클릭된 경우
                self.width = self.firstwidth - (mousex - self.clickmousex)
                self.height = self.firstheight + (mousey - self.clickmousey)
            if self.place[3]: # 왼쪽 위 클릭된 경우
                self.width = self.firstwidth - (mousex - self.clickmousex)
                self.height = self.firstheight - (mousey - self.clickmousey)
    def click(self, mousex, mousey, clicked, r_clicked):
        if self.x-self.width/2 <= mousex <= self.x+self.width/2 and self.y - self.height/2 <= mousey <= self.y + self.height/2: # 장애물 좌표 안에 마우스 좌표가 있으면 True 반환
            if clicked:
                return True
            if r_clicked: # 오른쪽 마우스 클릭된 경우 위치에 따라 리스트에 참 거짓을 저장할 것이다.
                if mousex >= self.x and mousey <= self.y: # 오른쪽 위 클릭된 경우
                    self.place[0] = True
                if mousex >= self.x and mousey >= self.y: # 오른쪽 아래 클릭된 경우
                    self.place[1] = True
                if mousex <= self.x and mousey >= self.y: # 왼쪽 아래 클릭된 경우
                    self.place[2] = True
                if mousex <= self.x and mousey <= self.y: # 왼쪽 위 클릭된 경우
                    self.place[3] = True
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
                objorder.append(len(objarr)-1)
            if 500 < mousex < 600 and 20 < mousey < 80: # rectangle 안에 클릭했으면
                obsarr.append(Obstacle()) # 장애물 append
                obsorder.append(len(obsarr)-1)

objarr = []
obsarr = []
objorder = [] # 클릭했을 때 가장 위로 올라오게 하는 리스트
obsorder = []
palette = Palette()

def changeObjorder(n): # 클릭했을 때 물체를 가장 위로 올라오게 하는 함수
    global objorder # objorder라는 리스트를 통해 컨트롤
    if objorder[n] != 0: # 클릭한 물체가 가장 위에 있지 않는 경우
        objorder2 = [objorder[i] for i in range(len(objorder))]
        for i in range(objorder[n]):
            objorder2[objorder.index(i)] += 1
        objorder2[n] = 0 # 가장 위로 올려보냄
        objorder = objorder2

def changeObsorder(n): # 클릭했을 때 장애물을 가장 위로 올라오게 하는 함수
    global obsorder # obsorder라는 리스트를 통해 컨트롤
    if obsorder[n] != 0: # 클릭한 장애물이 가장 위에 있지 않는 경우
        obsorder2 = [obsorder[i] for i in range(len(obsorder))]
        for i in range(obsorder[n]):
            obsorder2[obsorder.index(i)] += 1
        obsorder2[n] = 0 # 가장 위로 올려보냄
        obsorder = obsorder2

def MoveAllObj(mousex, mousey, clicked, r_clicked):
    anyselected = False
    for i in range(len(objarr)): # 클릭된게 하나라도 있는지 확인
        # 한번에 여러개 클릭 못하게 하려고 하는 작업
        if objarr[i].selected:
            anyselected = True
            break
    if anyselected: # 클릭된게 하나라도 있을 경우
        if objarr[i].click(mousex, mousey, clicked, False):
            objarr[i].selected = not objarr[i].selected
    if not anyselected: # 클릭된게 하나도 없었던 상황에서
        for i in range(len(objarr)):
            if objarr[objorder.index(i)].click(mousex, mousey, clicked, False): # 클릭되면
                j = objorder.index(i)
                changeObjorder(j)
                objarr[j].selected = not objarr[j].selected # 선택함
                objarr[j].firstplacex, objarr[j].firstplacey = objarr[j].x, objarr[j].y # 상대적 좌표로 움직이게 하려고 하는 작업
                objarr[j].clickmousex, objarr[j].clickmousey = mousex, mousey # 상대적 좌표로 움직이게 하려고 하는 작업
                break
            if objarr[objorder.index(i)].click(mousex, mousey, False, r_clicked):
                objarr[objorder.index(i)].initevery(objorder.index(i)+1)
    for i in range(len(objarr)-1, -1, -1): # 순서대로 이동시키고 출력
        objarr[objorder.index(i)].move(mousex, mousey)
        objarr[objorder.index(i)].show()

def MoveAllObs(mousex, mousey, clicked, r_clicked): # MoveAllObj와 거의 동일함
    anyselected = False
    anyr_selected = False # 오른쪽 마우스 클릭된 경우에 대한 변수
    for i in range(len(obsarr)):
        if obsarr[i].selected:
            anyselected = True
            break
        if obsarr[i].r_selected:
            anyr_selected = True
            break
    if anyselected:
        if obsarr[i].click(mousex, mousey, clicked, False):
            obsarr[i].selected = not obsarr[i].selected
    if anyr_selected: # 오른쪽 마우스 클릭된게 하나라도 있으면
        if obsarr[i].click(mousex, mousey, False, r_clicked): # 오른쪽 마우스를 다시 클릭했을 때
            obsarr[i].r_selected = not obsarr[i].r_selected # 클릭을 취소함
            obsarr[i].place = [False, False, False, False]
    if not anyselected and not anyr_selected:
        for i in range(len(obsarr)):
            if obsarr[obsorder.index(i)].click(mousex, mousey, clicked, False):
                j = obsorder.index(i)
                changeObsorder(j)
                obsarr[j].selected = not obsarr[j].selected
                obsarr[j].firstplacex, obsarr[j].firstplacey = obsarr[j].x, obsarr[j].y
                obsarr[j].clickmousex, obsarr[j].clickmousey = mousex, mousey
                break
            if obsarr[obsorder.index(i)].click(mousex, mousey, False, r_clicked):
                j = obsorder.index(i)
                changeObsorder(j)
                obsarr[j].r_selected = not obsarr[j].r_selected
                obsarr[j].firstplacex, obsarr[j].firstplacey = obsarr[j].x, obsarr[j].y
                obsarr[j].clickmousex, obsarr[j].clickmousey = mousex, mousey
                obsarr[j].firstwidth, obsarr[j].firstheight = obsarr[j].width, obsarr[j].height # 상대적 좌표로 크기 조절하려고 하는 작업
                break
    for i in range(len(obsarr)-1, -1, -1):
        obsarr[obsorder.index(i)].move(mousex, mousey)
        obsarr[obsorder.index(i)].show()

while True:
    clicked = False
    r_clicked = False
    screen.fill(WHITE)
    mousex, mousey = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == LEFT:
                clicked = True # clicked True
            if event.button == RIGHT:
                r_clicked = True
    palette.show() # palette 보여주고
    palette.clicked(mousex, mousey, clicked) # 팔레트 클릭되었는지 확인하고
    MoveAllObs(mousex, mousey, clicked, r_clicked) # 장애물 다 움직이고
    MoveAllObj(mousex, mousey, clicked, r_clicked) # 물체 다 움직임
    fpsClock.tick(FPS)
    pygame.display.flip()
