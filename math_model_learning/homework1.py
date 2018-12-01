import  numpy as np
import matplotlib.pyplot as plt
x=np.random.randint(1,100,size=(10,2))
np.savetxt("test_num.txt",x)
y1,y2=np.loadtxt("test_num.txt",delimiter=' ',unpack=True)
# print(np.max(y))
# print(np.min(y))
# print((np.mean(y)))
# print(np.cov(y))
# z=np.sort(y)
# print(z)
# print(y.sort())
# print(y1)
# print(y2)
index=np.arange(10)
bar_width=0.4
# plt.bar(index,y1,bar_width,color='r')
# plt.bar(index+bar_width,y2,bar_width,color='b')
# plt.bar(x=index,height=y1,width=bar_width,color='r')
# plt.bar(x=index,height=y2,width=bar_width,color='b',bottom=y1)
plt.barh(index,y1,bar_width,color='r')
plt.barh(index,y2,bar_width,color='b',left=y1)
plt.show()

