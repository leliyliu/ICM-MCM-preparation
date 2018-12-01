import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def func(x):
    return -(x-2)*(x-8)+40

a=2
b=9

x=np.linspace(0,10)
y=func(x)
fig,ax=plt.subplots()

ax.set_xticks([a,b])
ax.set_yticks([])
ax.set_xticklabels(['$ a $','$ b $'])

x1=np.linspace(2,9)
y1=func(x1)
ixy=zip(x1,y1)
points=[(a,0)]+list(ixy)+[(b,0)]#这里还要注意点的顺序的问题，不能随意取点
#p=np.array(points)

poly=mpatches.Polygon(points,facecolor='0.8',edgecolor='0.5')
ax.add_patch(poly)

plt.figtext(0.9,0.05,'$ x $')
plt.figtext(0.1,0.9,'$ y $')

plt.plot(x,y,'r','--',linewidth=2)

x_math=(a+b)/2
y_math=35
plt.text(x_math,y_math,r"$ \int_a^b(-(x-2)*(x-8)+40)dx $",size=10,horizontalalignment='center')

plt.show()