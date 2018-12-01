#箱型图 为了显示数据的分散情况  概率论中需要了解的
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(100)

data=np.random.normal(size=(100,5),loc=10,scale=10)
labels=['A','B','C','D','E']
plt.boxplot(data,sym='o',labels=labels)#whis用来判断异常值

plt.show()
