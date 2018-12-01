import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
fig,ax=plt.subplots()

xy1=np.array([0.2,0.2])
xy2=np.array([0.2,0.8])
xy3=np.array([0.8,0.2])
xy4=np.array([0.8,.8])

circle=mpatches.Circle(xy1,0.05)
rect=mpatches.Rectangle(xy2,0.2,0.1,color='r')
ploygon=mpatches.RegularPolygon(xy3,5,0.1,color='g')#正多边形
ellipse=mpatches.Ellipse(xy4,0.4,0.2,color='y')#长轴短轴，而不是长半轴短半轴


ax.add_patch(circle)
ax.add_patch(rect)
ax.add_patch(ploygon)
ax.add_patch(ellipse)

plt.axis("equal")
plt.grid()

plt.show()