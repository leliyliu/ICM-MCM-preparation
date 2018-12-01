import matplotlib.pyplot as plt
import numpy as np
from  numpy import  random as nr
# #这里画的是直方图，注意和work1中条形图的区别
# mu=100
# sigma=20
# x=nr.normal(mu,sigma,size=(20000,1))#注意和randn的区别
# plt.hist(x,bins=200,color='r',normed=False)#normed表示频率
# plt.show()
# x=nr.randn(1000)+2
# y=nr.randn(1000)+3
#
# plt.hist2d(x,y,bins=40)
# plt.show()#双变量的分布图

mu=10
sigma=3
x=mu+sigma*nr.randn(2000)
plt.subplot(221)
plt.hist(x,bins=10,normed=True)
plt.subplot(222)
plt.hist(x,bins=50,normed=False)
y1=1+nr.randn(2000)
y2=5+nr.randn(2000)
plt.subplot(212)
plt.hist2d(y1,y2,bins=40)
plt.show()