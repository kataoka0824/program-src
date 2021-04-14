import random
import csv
import numpy as np
def main():
	data=[]
	data1=[]
	with open("gakusyudata.csv","r") as f:
		reader=csv.reader(f)
		for row in reader:
			data1.append(row)
		for i in range(15):
			data.append([int(n) for n in data1[i]])
		print(data)
		for i in range(15):
			print(sum(data[i]))
	block=input("block:rlud")
	if block=="0000":
		a=np.random.choice(["r","l","u","d"],p=[data[0][0]/sum(data[0]),data[0][1]/sum(data[0]),data[0][2]/sum(data[0]),data[0][3]/sum(data[0])])
		print(a)
	if block=="0001":
		a=np.random.choice(["r","l","u"],p=[data[1][0]/sum(data[1]),data[1][1]/sum(data[1]),data[1][2]/sum(data[1])])
		print(a)
	if block=="0010":
		a=np.random.choice(["r","l","d"],p=[data[2][0]/sum(data[2]),data[2][1]/sum(data[2]),data[2][2]/sum(data[2])])
		print(a)
	if block=="0100":
		a=np.random.choice(["r","u","d"],p=[data[3][0]/sum(data[3]),data[3][1]/sum(data[3]),data[3][2]/sum(data[3])])
		print(a)
	if block=="1000":
		a=np.random.choice(["l","u","d"],p=[data[4][0]/sum(data[4]),data[4][1]/sum(data[4]),data[4][2]/sum(data[4])])
		print(a)
	if block=="0011":
		a=np.random.choice(["r","l"],p=[data[5][0]/sum(data[5]),data[5][1]/sum(data[5])])
		print(a)
	if block=="0101":
		a=np.random.choice(["r","u"],p=[data[6][0]/sum(data[6]),data[6][1]/sum(data[6])])
		print(a)
	if block=="1001":
		a=np.random.choice(["l","u"],p=[data[7][0]/sum(data[7]),data[7][1]/sum(data[7])])
		print(a)
	if block=="0110":
		a=np.random.choice(["r","d"],p=[data[8][0]/sum(data[8]),data[8][1]/sum(data[8])])
		print(a)
	if block=="1010":
		a=np.random.choice(["l","d"],p=[data[9][0]/sum(data[9]),data[9][1]/sum(data[9])])
		print(a)
	if block=="1100":
		a=np.random.choice(["u","d"],p=[data[10][0]/sum(data[10]),data[10][1]/sum(data[10])])
		print(a)
	if block=="0111":
		a=np.random.choice(["r"],p=[data[11][0]/sum(data[11])])
		print(a)
	if block=="1011":
		a=np.random.choice(["l"],p=[data[12][0]/sum(data[12])])
		print(a)
	if block=="1101":
		a=np.random.choice(["u"],p=[data[13][0]/sum(data[13])])
		print(a)
	if block=="1110":
		a=np.random.choice(["d"],p=[data[14][0]/sum(data[14])])
		print(a)
if __name__=="__main__":
	main()
