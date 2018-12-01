import matplotlib.pyplot as plt
import numpy as np

# x=np.arange(-10,11,1)
#
# y=x*x
#
# plt.plot(x,y)

# plt.annotate('this is the bottom',xy=(0,1),xytext=(0,20),arrowprops=dict(facecolor='r',headlength=5,headwidth=20,width=10))#注意理解这几个参数的含义

#plt.text(-4,40,'function:y=x*x',family='fantasy',size=20,color='r',style='italic',weight='bold',bbox=dict(facecolor='c',alpha=0.2))#相当于设置一个插入文本框
#前两个参数表示的是坐标，而family表示的是字体,size表示字的大小，style表示是否为斜体，weight表示粗细，bbox表示的是外框，facecolor颜色，alpha透明度

fig=plt.figure()

ax=fig.add_subplot(111)

ax.set_xlim([1,7])
ax.set_ylim([1,5])

ax.text(2,4,r"$ \alpha_i \beta_j \pi \lambda \omega $",size=20)#采用面向对象的方式
ax.text(4,4,r"$ \sin(0)=\cos(\frac{\pi}{2}) $",size=20)
ax.text(2,2,r"$ \lim_{x \rightarrow y} \frac{1}{x^3} $",size=20)
ax.text(4,2,r"$ \sqrt[4]{x}=\sqrt{y} $",size=20)
## r表示不转义

plt.show()