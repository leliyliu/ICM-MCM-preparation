#饼状图
import matplotlib.pyplot as plt

labels='A','B','C','D'
fracs=[15,30,45,10]

explode=[0,0,0.05,0]#设置与中心的远离

plt.axes(aspect=1)#设置x,y，使其成为一个圆

plt.pie(x=fracs,labels=labels,autopct='%.1f%%',explode=explode,shadow=True)

plt.show()