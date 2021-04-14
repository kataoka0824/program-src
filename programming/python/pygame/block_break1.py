import pygame
from pygame.locals import *
import sys
(w,h)=(800,600)
mt=0
t=0
bt=0
bl_x_pos=15
bl_y_pos=4
bl_pos=[[0 for i in range(bl_y_pos)] for j in range(bl_x_pos)]
bl_pos_jud=[[1 for i in range(bl_y_pos)] for j in range(bl_x_pos)]
bar_x=0
ball_x=0
ball_y=0
ball_xv=6
ball_yv=6
bar_y=580
start_jud=0
def bar_ref(ball_x,ball_y,ball_xv,ball_yv,bar_x,bar_y):
    #if ball_x>bar_x-34 and ball_x<bar_x-17 and ball_y>bar_y-9 and ball_y<bar_y+6:
    #    ball_xv=-0.4
    #    ball_yv=-0.1
    #if ball_x>bar_x-17 and ball_x<bar_x and ball_y>bar_y-9 and ball_y<bar_y+6:
    #    ball_xv=-0.2
    #    ball_yv=-0.2
    #if ball_x>bar_x and ball_x<bar_x+17 and ball_y>bar_y-9 and ball_y<bar_y+6:
    #    ball_xv=0.2
    #    ball_yv=-0.2
    #if ball_x>bar_x+17 and ball_x<bar_x+34 and ball_y>bar_y-9 and ball_y<bar_y+6:
    #    ball_xv=0.4
    #    ball_yv=-0.1
    for i in range(14):
        i2=float(i)
        if ball_x>bar_x+(i2-7)*5 and ball_x<bar_x+(i2-6)*5 and ball_y>bar_y-9 and ball_y<bar_y+6:
            if i==0:
                ball_xv=-3
                ball_yv=-1
            if i<7 and i>0:
                ball_xv=(-0.35+i2*0.05)*10
                ball_yv=(-0.1-i2*0.05)*10
            if i>=7 and i<13:
                ball_xv=(-0.30+i2*0.05)*10
                ball_yv=(-0.30+(i2-7)*0.05)*10
            if i==13:
                ball_xv=3
                ball_yv=-1
    return ball_xv,ball_yv
def kabe_ref(ball_x,ball_y,ball_xv,ball_yv,w,h):
    if ball_x<0 or ball_x>w:
        ball_xv=-ball_xv
    if ball_y<0:
        ball_yv=-ball_yv
    return ball_xv,ball_yv
def block_ref(ball_x,ball_y,ball_xv,ball_yv,b_x,b_y,bl_pos_jud):
    if ball_x>b_x-25 and ball_x<b_x+25 and ball_y>b_y-15 and ball_y<b_y+15 and bl_pos_jud==1:
        bl_pos_jud=0
        if ball_x>b_x+22 and ball_x<b_x+25 and bl_pos_jud==0 and ball_xv<0:
            ball_xv=-ball_xv
        if ball_y>b_y+11 and ball_y<b_y+15 and bl_pos_jud==0 and ball_yv<0:
            ball_yv=-ball_yv
        if ball_x<b_x-22 and ball_x>b_x-25 and bl_pos_jud==0 and ball_xv>0:
            ball_xv=-ball_xv
        if ball_y<b_y-11 and ball_y>b_y-15 and bl_pos_jud==0 and ball_yv>0:
            ball_yv=-ball_yv
    return ball_xv,ball_yv,bl_pos_jud
def break_block(ball_x,ball_y,ball_xv,ball_yv,bl_pos_jud):
    for i in range(bl_x_pos):
        for j in range(bl_y_pos):
            ball_xv,ball_yv,bl_pos_jud[i][j]=block_ref(ball_x,ball_y,ball_xv,ball_yv,50*(i+1),30*(j+1),bl_pos_jud[i][j])
    return ball_xv,ball_yv,bl_pos_jud
def time(mt,t):
    if mt>1:
        t=t+1
        mt=0
        print("mt:",mt,"t:",t)
    return mt,t
def ball_move(ball_x,ball_y,ball_xv,ball_yv):
    ball_x=ball_x+ball_xv
    ball_y=ball_y+ball_yv
    return ball_x,ball_y
def block_base(b_x,b_y,bl_pos_jud):
    if bl_pos_jud==1:
        pygame.draw.rect(screen,(255,25,25),Rect(b_x-20,b_y-10,40,20))
def block_make(bl_pos,bl_pos_jud):
    for i in range(bl_x_pos):
        for j in range(bl_y_pos):
            bl_pos[i][j]=block_base(50*(i+1),30*(j+1),bl_pos_jud[i][j])
    return bl_pos,bl_pos_jud
def bar(bar_x,bar_y):
    pygame.draw.rect(screen,(25,25,255),Rect(bar_x-30,bar_y-4,60,8))
def ball(ball_x,ball_y):
    pygame.draw.ellipse(screen,(255,255,255),(ball_x,ball_y,10,10))
def start_jud1(start_jud,bar_x,bar_y,ball_x,ball_y):
    if start_jud==0:
        ball_x=bar_x
        ball_y=bar_y-9
    return start_jud,ball_x,ball_y
def show_info(screen,t):
    font = pygame.font.Font(None, 35)
    text = font.render("t:", True, (255,255,255))
    text2 = font.render(str(t), True, (255,255,255))
    screen.blit(text, [700, 10])
    screen.blit(text2, [730, 10])
#def game_over(screen):
pygame.init()
screen=pygame.display.set_mode((w,h))
while (1):
    mt=mt+0.01
    mt,t=time(mt,t)
    bl_pos,bl_pos_jud=block_make(bl_pos,bl_pos_jud)
    bar(bar_x,bar_y)
    ball_x,ball_y=ball_move(ball_x,ball_y,ball_xv,ball_yv)
    ball(ball_x,ball_y)
    ball_xv,ball_yv=kabe_ref(ball_x,ball_y,ball_xv,ball_yv,w,h)
    ball_xv,ball_yv=bar_ref(ball_x,ball_y,ball_xv,ball_yv,bar_x,bar_y)
    ball_xv,ball_yv,bl_pos_jud=break_block(ball_x,ball_y,ball_xv,ball_yv,bl_pos_jud)
    start_jud,ball_x,ball_y=start_jud1(start_jud,bar_x,bar_y,ball_x,ball_y)
    show_info(screen,t)
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:  # 閉じるボタンが押されたら終了
            pygame.quit()       # Pygameの終了(画面閉じられる)
            sys.exit()
            # キーを押したとき
        if event.type == KEYDOWN:
            # ESCキーなら終了
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == 'q':
                pygame.quit()
                sys.exit()
        if event.type==MOUSEMOTION:
            bar_x,bar_y_sub=event.pos
        if event.type==MOUSEBUTTONDOWN:
            start_jud=1
    pygame.display.update()     # 画面を更新
    pygame.time.wait(10) 
    screen.fill((0,0,0))
