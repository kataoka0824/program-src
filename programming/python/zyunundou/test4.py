import numpy as np
import sys
import math
global A
def cos(rad):
	return round(math.cos(rad),6)
def sin(rad):
	return round(math.sin(rad),6)
def make_r_x(rad):
	a=[[1,0,0],[0,cos(rad),sin(rad)],[0,sin(rad),cos(rad)]]
	return a
def make_r_y(rad):
	a=[[cos(rad),0,sin(rad)],[0,1,0],[-sin(rad),0,cos(rad)]]
	return a
def make_r_z(rad):
	a=[[cos(rad),sin(rad),0],[sin(rad),cos(rad),0],[0,0,1]]
	return a
def count():
	k=int(input("リンク数:"))
	return k
def make_rad(i):
	print("deg"+str(i+1)+"=",end="")
	deg=float(input())
	rad=math.radians(deg)
	return rad
def make_axis(i):
	jud=0
	while jud==0:
		axis=input("回転軸(x,y,z)["+str(i+1)+"]:")
		if axis=="x" or axis=="y" or axis=="z":
			jud=1
	return axis
def make_axis_l(i):
	jud=0
	while jud==0:
		axis=input("リンク軸(x,y,z)["+str(i+1)+"]:")
		if axis=="x" or axis=="y" or axis=="z":
			jud=1
	return axis
def make_syoki():
	axis_1=make_axis_l(-1)
	l1=float(input("l0="))
	if axis_1=="x":
		l=[l1,0,0]
	if axis_1=="y":
		l=[0,l1,0]
	if axis_1=="z":
		l=[0,0,l1]
	return l
def make_l(i):
	axis_1=make_axis_l(i)
	l1=float(input("l"+str(i+1)+"="))
	if axis_1=="x":
		l=[l1,0,0]
	if axis_1=="y":
		l=[0,l1,0]
	if axis_1=="z":
		l=[0,0,l1]
	return l
def main():
	rad=[]
	a_x=[]
	a_y=[]
	a_z=[]
	a=[]
	axis=[]
	l=[]
	l.append(make_syoki())
	A1=[[1,0,0],[0,1,0],[0,0,1]]
	A=[0,0,0]
	log_A=[]
	k=count()
	for i in range(k):
		rad.append(make_rad(i))
		axis.append(make_axis(i))
		a_x.append(make_r_x(rad[i]))
		a_y.append(make_r_y(rad[i]))
		a_z.append(make_r_z(rad[i]))
		l.append(make_l(i))
		if axis[i]=="x":
			a.append(a_x[i])
		if axis[i]=="y":
			a.append(a_y[i])
		if axis[i]=="z":
			a.append(a_z[i])
	for i in range(k+1):
		for j in range(i):
			A1=np.dot(A1,a[j])
		A1=np.dot(A1,l[k-i])
		A+=A1
		log_A.append(A1)
		A1=[[1,0,0],[0,1,0],[0,0,1]]
	print(A)
	print(log_A)
	#print(rad)
	#print(axis)
	#print(a[0])
	#print(l)
	
if __name__=="__main__":
	main()
