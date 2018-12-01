import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#plt.style.use('ggplot')#show by plt.style.available
plt.style.use('fivethirtyeight')

fig,axes=plt.subplots(2,2)
ax1,ax2,ax3,ax4=axes.ravel()

x,y=np.random.normal(size=(2,100))
ax1.plot(x,y,'o')

x=np.arange(0,10)
y=np.arange(0,10)

#ncolors=len(plt.rcParams['axes.color_cycle'])
#设置颜色的循环   在后续的rcParams中，已经无此参数，所以不用再考虑
#但是这里需要注意，rcParams是一个十分有用的工具，在设置图形中起到巨大作用 也可以通过plt.rcParams.keys()来查看内容


shift=np.linspace(0,10,7)

for s in shift:
    ax2.plot(x,y+s,'-')

x=np.arange(5)
y1,y2,y3=np.random.randint(1,25,size=(3,5))
width=.25

ax3.bar(x,y1,width,color='y')
ax3.bar(x+width,y2,width,color='r')
ax3.bar(x+2*width,y3,width,color='c')

for i,color in enumerate(['b','g','r','c','m','y','k']):
    xy=np.random.normal(size=2)
    ax4.add_patch(plt.Circle(xy,radius=0.3,color=color))
ax4.axis('equal')

plt.show()
