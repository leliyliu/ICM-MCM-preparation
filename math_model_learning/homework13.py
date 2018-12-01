import matplotlib.pyplot as plt
import numpy as np

#r=np.arange(1,6,1)
r=5*np.ones(shape=[9,1])

#theta=[0,np.pi/2,np.pi,3*np.pi/2,2*np.pi]
theta=[]
for i in range(9):
    theta.append(np.pi*i/4)

ax=plt.subplot(111,projection='polar')#以极坐标的形式来画图

ax.plot(theta,r,color='r',linewidth=3)
ax.grid(True)
plt.show()