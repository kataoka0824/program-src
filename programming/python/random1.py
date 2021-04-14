import random
import math
import sys
jud=0
n = int(sys.argv[1])
for i in range(n):
    x=random.random()
    y=random.random()
    r=math.sqrt(x**2+y**2)
    if r<1:
        jud+=1

print("pi:",jud/n*4)
