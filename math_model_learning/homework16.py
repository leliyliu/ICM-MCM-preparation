# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.font_manager import FontProperties
plt.style.use('ggplot')


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

#注意用来解决中文输出的方法

ability_label=[u'进攻',u'防守',u'盘带',u'速度',u'体力',u'射术']
ability_size=6

#font=FontProperties()

ax1=plt.subplot(221,projection='polar')
ax2=plt.subplot(222,projection='polar')
ax3=plt.subplot(223,projection='polar')
ax4=plt.subplot(224,projection='polar')



player={'M':np.random.randint(size=ability_size,low=60,high=99),
        'H': np.random.randint(size=ability_size, low=60, high=99),
        'P': np.random.randint(size=ability_size, low=60, high=99),
        'Q': np.random.randint(size=ability_size, low=60, high=99)}

theta=np.linspace(0,2*np.pi,6,endpoint=False)
theta=np.append(theta,theta[0])

player['M']=np.append(player['M'],player['M'][0])
player['H']=np.append(player['H'],player['H'][0])
player['P']=np.append(player['P'],player['P'][0])
player['Q']=np.append(player['Q'],player['Q'][0])

axs=[ax1,ax2,ax3,ax4]
names=[u'梅西',u'哈维',u'皮克',u'切赫']
players=['M','H','P','Q']
colors=['r','g','b','y']

for ax,elec,color,name in zip(axs,players,colors,names):
    ax.plot(theta,player[elec],color)
    ax.fill(theta,player[elec],color,alpha=0.3)
    ax.set_xticks(theta)
    ax.set_yticks([20,40,60,80,100])
    ax.set_xticklabels(ability_label)
    ax.set_title(name,position=(0.5,1),size=12,color=color)

# ax1.plot(theta,player['M'],'r')
# ax1.fill(theta,player['M'],'r',alpha=0.3)
# ax1.set_xticks(theta)
# ax1.set_yticks([20,40,60,80,100])
# ax1.set_xticklabels(ability_label)
# ax1.set_title('梅西',position=(0.5,1),size=12,color='r')
#
# ax2.plot(theta,player['H'],'g')
# ax2.fill(theta,player['H'],'g',alpha=0.3)
# ax2.set_xticks(theta)
# ax2.set_yticks([20,40,60,80,100])
# ax2.set_xticklabels(ability_label)
# ax2.set_title('哈维',position=(0.5,1),size=12,color='g')
#
# ax3.plot(theta,player['P'],'b')
# ax3.fill(theta,player['P'],'b',alpha=0.3)
# ax3.set_xticks(theta)
# ax3.set_yticks([20,40,60,80,100])
# ax3.set_xticklabels(ability_label)
# ax3.set_title('皮克',position=(0.5,1),size=12,color='b')
#
# ax4.plot(theta,player['Q'],'y')
# ax4.fill(theta,player['Q'],'y',alpha=0.3)
# ax4.set_xticks(theta)
# ax4.set_yticks([20,40,60,80,100])
# ax4.set_xticklabels(ability_label)
# ax4.set_title('切赫',position=(0.5,1),size=12,color='y')


plt.show()