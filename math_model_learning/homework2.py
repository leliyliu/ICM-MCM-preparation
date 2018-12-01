import numpy as np
import matplotlib.pyplot as plt
N=5
y=[20,10,30,25,15]
index=np.arange(N)
plt.bar(left=0,bottom=index,width=y,color='red',height=0.5,orientation='horizontal')
plt.barh(left=0,bottom=index,width=y)
plt.xlabel("x")
plt.ylabel('y')
plt.show()
