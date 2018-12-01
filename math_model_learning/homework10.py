import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,5*np.pi,1000)

y1=np.sin(x)
y2=np.sin(2*x)

# plt.plot(x,y1)
# plt.plot(x,y2)

#plt.xlim([0,16])

# plt.fill(x,y1,'b',alpha=.3)
# plt.fill(x,y2,'r',alpha=.3)

fig=plt.figure()
ax=plt.gca()

ax.plot(x,y1,x,y2,color='black')


ax.fill_between(x,y1,y2,where=y1>y2,facecolor='b',interpolate=True)
ax.fill_between(x,y1,y2,where=y2>y1,facecolor='c',interpolate=True)
#1.注意where的使用方法，以及facecolor，而对于interpolate而言，则是说，如果interpolate为True，那么会自动补全中间无法判断的值

plt.show()