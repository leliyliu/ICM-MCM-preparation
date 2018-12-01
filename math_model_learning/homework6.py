# from pylab import *
#
# x=arange(0,10,1)
# y=randn(len(x))
#
# plot(x,y)
#
# title("pylab")
#
# show()

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,1)
y=np.random.randn(len(x))

fig=plt.figure() #构建一个对象，而对其进行绘图

ax=fig.add_subplot(111)

plt.plot(x,y)

t=ax.set_title('object oriented')

plt.show()