import numpy as np
import sys
import math

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
def main():
	deg=float(input("deg="))
	rad=math.radians(deg)
	a_x=make_r_x(rad)
	a_y=make_r_y(rad)
	a_z=make_r_z(rad)
	print(a_x)
	print(a_y)
	print(a_z)
	
if __name__=="__main__":
	main()
