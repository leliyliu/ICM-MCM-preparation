import  numpy as np
import  matplotlib.pyplot as plt
x=np.arange(2,20,1)
y1=x*x
y2=np.log(x)
# plt.plot(x,y1)
# plt.twinx()
# plt.plot(x,y2,color='r')
# plt.show()
fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(x,y1,label='function(y1)')
ax1.set_ylabel('Y1')
ax2=fig.add_subplot(111)
ax2=ax1.twinx()
ax2.plot(x,y2,'r',label='function(y2)')
ax2.set_ylabel('Y2')
fig.legend()
plt.show()
