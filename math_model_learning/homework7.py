import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime

fig=plt.figure()

start=datetime.datetime(2015,1,1)
stop=datetime.datetime(2016,1,1)
delta=datetime.timedelta(days=1)

dates=mpl.dates.drange(start,stop,delta)

y=np.random.rand(len(dates))

ax=plt.gca()

ax.plot_date(dates,y,linestyle='-',marker=' ')

date_format=mpl.dates.DateFormatter('%Y-%m-%d')#设置日期格式

fig.autofmt_xdate()#自适应大小和角度

ax.locator_params('x',nbins=12)

ax.xaxis.set_major_formatter(date_format)

plt.show()