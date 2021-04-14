import pygame
from pygame.locals import *
import sys
import random

def main():
	(rand_ta,rand_yo)=([],[])
	(w,h) = (600,600)   # 画面サイズ
	#(x,y) = (w//2, h//2)
	(x,y) = (20, h//2)
	(ta,yo) = (w//15,h//15)
	(ta_g,yo_g)=(random.randint(0,14),random.randint(0,14))
	(log_x,log_y)=([20],[h//2])
	bl_j=[]
	bl_j_g=0
	cl_key=0
	k=0
	for i in range(50):
		bl_j.append(0)
	pygame.init()       # pygame初期化
	pygame.display.set_mode((w, h), 0, 32)  # 画面設定
	screen = pygame.display.get_surface()
	jud=0
	for i in range(50):
		rand_ta.append(random.randint(0,14))
		rand_yo.append(random.randint(0,14))
		if rand_ta[i]==0 and rand_yo[i]==7:
			rand_ta[i]=random.randint(0,14)
			rand_yo[i]=random.randint(0,14)
		if rand_ta[i]==ta_g and rand_yo[i]==yo_g:
			rand_ta[i]=random.randint(0,14)
			rand_yo[i]=random.randint(0,14)
	while (1):
		pygame.display.update()     # 画面更新
		pygame.time.wait(30)        # 更新時間間隔
		screen.fill((0, 20, 0, 0))  # 画面の背景色
        # 円の中心座標が画面の範囲外にある場合
		if x < 20:
			x = 20
		if x > w-20:
			x = w-20
		if y < 20:
			y = 20
		if y > h-20:
			y = h-20
        # ブロック生成 サーチ
		for i in range(50):
			if bl_j[i]==0:
				pygame.draw.rect(screen,(0,0,0),Rect(ta*rand_ta[i],yo*rand_yo[i],40,40))
			if x>ta*rand_ta[i]-40 and y<yo*rand_yo[i]+80 and x<ta*rand_ta[i]+80 and y>yo*rand_yo[i]-40:
				bl_j[i]=1
			if bl_j[i]==1:
				pygame.draw.rect(screen,(255,0,0),Rect(ta*rand_ta[i],yo*rand_yo[i],40,40))
			if x>ta*rand_ta[i] and y<yo*rand_yo[i]+40 and x<ta*rand_ta[i]+40 and y>yo*rand_yo[i]:
				pygame.draw.rect(screen,(255,255,255),Rect(ta*rand_ta[i],yo*rand_yo[i],40,40))
	# 通ったルート
		for i in range(k):
			pygame.draw.rect(screen,(100,150,150),Rect(log_x[i]-20,log_y[i]-20,40,40))
	# 正解ブロック サーチ
		if bl_j_g==0:
			pygame.draw.rect(screen,(0,0,0),Rect(ta*ta_g,yo*yo_g,40,40))
		if x>ta*ta_g-40 and y<yo*yo_g+80 and x<ta*ta_g+80 and y>yo*yo_g-40:
			bl_j_g=1
		if bl_j_g==1:
			pygame.draw.rect(screen,(0,200,200),Rect(ta*ta_g,yo*yo_g,40,40))
		if x>ta*ta_g and y<yo*yo_g+40 and x<ta*ta_g+40 and y>yo*yo_g:
			pygame.draw.rect(screen,(255,255,255),Rect(ta*ta_g,yo*yo_g,40,40))
			print("ゴールまでの移動回数:",cl_key)
			pygame.quit()
			sys.exit()
	# 円を描画
		pygame.draw.circle(screen, (0, 200, 0), (x, y), 20)
	# 罫線
		for i in range(15):
			for j in range(15):
				pygame.draw.rect(screen,(255,255,255),Rect(ta*i,yo*j,40,40),2)
        # イベント処理
		for event in pygame.event.get():
            # 画面の閉じるボタンを押したとき
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
            # キーを押したとき
			if event.type == KEYDOWN:
                # ESCキーなら終了
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
                # 矢印キーなら円の中心座標を矢印の方向に移動
				if event.key == K_LEFT:
					x -= 40
					cl_key+=1
					log_x.append(x)
					log_y.append(y)
				if event.key == K_RIGHT:
					x += 40
					cl_key+=1
					log_x.append(x)
					log_y.append(y)
				if event.key == K_UP:
					y -= 40
					cl_key+=1
					log_x.append(x)
					log_y.append(y)
				if event.key == K_DOWN:
					y += 40
					cl_key+=1
					log_x.append(x)
					log_y.append(y)
				k+=1
if __name__ == "__main__":
	main()
