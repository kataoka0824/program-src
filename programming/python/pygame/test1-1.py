import pygame
from pygame.locals import *
import sys
import random
import csv
import numpy as np
def AI(b_r,b_l,b_u,b_d):
	data=[]
	data1=[]
	with open("gakusyudata.csv","r") as f:
		reader=csv.reader(f)
		for row in reader:
			data1.append(row)
		for i in range(15):
			data.append([int(n) for n in data1[i]])
	if b_r==0 and b_l==0 and b_u==0 and b_d==0:
		a=np.random.choice(["r","l","u","d"],p=[data[0][0]/sum(data[0]),data[0][1]/sum(data[0]),data[0][2]/sum(data[0]),data[0][3]/sum(data[0])])
		print(a)
	if b_r==0 and b_l==0 and b_u==0 and b_d==1:
		a=np.random.choice(["r","l","u"],p=[data[1][0]/sum(data[1]),data[1][1]/sum(data[1]),data[1][2]/sum(data[1])])
		print(a)
	if b_r==0 and b_l==0 and b_u==1 and b_d==0:
		a=np.random.choice(["r","l","d"],p=[data[2][0]/sum(data[2]),data[2][1]/sum(data[2]),data[2][2]/sum(data[2])])
		print(a)
	if b_r==0 and b_l==1 and b_u==0 and b_d==0:
		a=np.random.choice(["r","u","d"],p=[data[3][0]/sum(data[3]),data[3][1]/sum(data[3]),data[3][2]/sum(data[3])])
		print(a)
	if b_r==1 and b_l==0 and b_u==0 and b_d==0:
		a=np.random.choice(["l","u","d"],p=[data[4][0]/sum(data[4]),data[4][1]/sum(data[4]),data[4][2]/sum(data[4])])
		print(a)
	if b_r==0 and b_l==0 and b_u==1 and b_d==1:
		a=np.random.choice(["r","l"],p=[data[5][0]/sum(data[5]),data[5][1]/sum(data[5])])
		print(a)
	if b_r==0 and b_l==1 and b_u==0 and b_d==1:
		a=np.random.choice(["r","u"],p=[data[6][0]/sum(data[6]),data[6][1]/sum(data[6])])
		print(a)
	if b_r==1 and b_l==0 and b_u==0 and b_d==1:
		a=np.random.choice(["l","u"],p=[data[7][0]/sum(data[7]),data[7][1]/sum(data[7])])
		print(a)
	if b_r==0 and b_l==1 and b_u==1 and b_d==0:
		a=np.random.choice(["r","d"],p=[data[8][0]/sum(data[8]),data[8][1]/sum(data[8])])
		print(a)
	if b_r==1 and b_l==0 and b_u==1 and b_d==0:
		a=np.random.choice(["l","d"],p=[data[9][0]/sum(data[9]),data[9][1]/sum(data[9])])
		print(a)
	if b_r==1 and b_l==1 and b_u==0 and b_d==0:
		a=np.random.choice(["u","d"],p=[data[10][0]/sum(data[10]),data[10][1]/sum(data[10])])
		print(a)
	if b_r==0 and b_l==1 and b_u==1 and b_d==1:
		a=np.random.choice(["r"],p=[data[11][0]/sum(data[11])])
		print(a)
	if b_r==1 and b_l==0 and b_u==1 and b_d==1:
		a=np.random.choice(["l"],p=[data[12][0]/sum(data[12])])
		print(a)
	if b_r==1 and b_l==1 and b_u==0 and b_d==1:
		a=np.random.choice(["u"],p=[data[13][0]/sum(data[13])])
		print(a)
	if b_r==1 and b_l==1 and b_u==1 and b_d==0:
		a=np.random.choice(["d"],p=[data[14][0]/sum(data[14])])
		print(a)
	return a
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
	bl_l=0
	bl_r=0
	bl_u=0
	bl_d=0
	data1=[]
	data=[]
	state_bl=[]
	f_name="gamedata.csv"
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
		if x <= 20:
			x = 20
			bl_l=1
		if x >= w-20:
			x = w-20
			bl_r=1
		if y <= 20:
			y = 20
			bl_u=1
		if y >= h-20:
			y = h-20
			bl_d=1
        # ブロック生成 サーチ
		for i in range(50):
			if bl_j[i]==0:
				pygame.draw.rect(screen,(0,0,0),Rect(ta*rand_ta[i],yo*rand_yo[i],40,40))
			#全方向サーチ
			#if x>ta*rand_ta[i]-40 and y<yo*rand_yo[i]+80 and x<ta*rand_ta[i]+80 and y>yo*rand_yo[i]-40:
			#左サーチ
			if x>ta*rand_ta[i] and y<yo*rand_yo[i]+40 and x<ta*rand_ta[i]+80 and y>yo*rand_yo[i]:
				bl_j[i]=1
				bl_l=1
			#右サーチ
			if x>ta*rand_ta[i]-40 and y<yo*rand_yo[i]+40 and x<ta*rand_ta[i]+40 and y>yo*rand_yo[i]:
				bl_j[i]=1
				bl_r=1
			#下サーチ
			if x>ta*rand_ta[i] and y<yo*rand_yo[i]+40 and x<ta*rand_ta[i]+40 and y>yo*rand_yo[i]-40:
				bl_j[i]=1
				bl_d=1
			#上サーチ
			if x>ta*rand_ta[i] and y<yo*rand_yo[i]+80 and x<ta*rand_ta[i]+40 and y>yo*rand_yo[i]:
				bl_j[i]=1
				bl_u=1
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
			with open(f_name,"a") as f:
				writer = csv.writer(f,lineterminator="\n")
				writer.writerows(state_bl)
			print(state_bl)
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
					if bl_l==0:
						x -= 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"l"])
				if event.key == K_RIGHT:
					if bl_r==0:
						x += 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"r"])
				if event.key == K_UP:
					if bl_u==0:
						y -= 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"u"])
				if event.key == K_DOWN:
					if bl_d==0:
						y += 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"d"])
				print("log_x:",log_x[k]/40+0.5)
				print("log_y:",log_y[k]/40+0.5)
				print("bl_r:",bl_r,"bl_l:",bl_l,"bl_u",bl_u,"bl_d",bl_d)
				with open("gakusyudata.csv","r") as f_r:
					reader=csv.reader(f_r)
					for row in reader:
						data1.append(row)
					for i in range(15):
						data.append([int(n) for n in data1[i]])
				print(data)
				for i in range(15):
					print(sum(data[i]))
				if event.key == K_SPACE:
					state=AI(bl_r,bl_l,bl_u,bl_d)
					if state=="r":
						x += 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"r"])
					if state=="l":
						x -= 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"l"])
					if state=="u":
						y -= 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"u"])
					if state=="d":
						y += 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"d"])
				bl_l=0
				bl_r=0
				bl_u=0
				bl_d=0
	
						
if __name__ == "__main__":
	main()
