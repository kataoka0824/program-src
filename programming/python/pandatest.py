import pandas as pd
def main():
	a=[]
	ix=[]
	cs=[]
	k=int(input("k="))
	for i in range(k):
		a1=[]
		for j in range(k):
			print("a[%d][%d]=" % (i,j),end="")
			a1.append(int(input()))
		a.append(a1)
		ix.append("row"+str(i+1))
		cs.append("col"+str(i+1))
	#print(a)
	df=pd.DataFrame(a,
	index=ix,
	columns=cs
	)
	print(df)
if __name__=="__main__":
	main()
