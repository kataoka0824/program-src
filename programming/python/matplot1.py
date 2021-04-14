import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
 
x = [1, 2, 3, 4, 5]
y = [1, 8, 3, 6, 5]
z = [1, 5, 3, 8, 9]
 
ax.scatter(x, y, z, c='r', marker='^', label='test')
plt.plot(x,y,z,label='test',linewidth=3,color='b',
          marker='^',markeredgecolor="black")
ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
