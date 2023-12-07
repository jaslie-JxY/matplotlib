# 根据自己的实际情况,统计出来了最近20周和对象吵架的次数如列表a,请绘制出该数据的折线图
# 以便分析自己每年和对象吵架的数量走势a = [1,0,2,1,3,1,2,1,3,1,0,2,3,2,1,1,0,1,0,1]
# 要求: y轴表示吵架次数 x轴表示周数,比如第1周,第2周等
# 同时朋友每年和对象吵架的数量走势b = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
# 画在一个图像中对比查看分析

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")

x = range(1, 21)
y1 = a = [1, 0, 2, 1, 3, 1, 2, 1, 3, 1, 0, 2, 3, 2, 1, 1, 0, 1, 0, 1]
y2 = b = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]

plt.figure(figsize=(17, 7.7))

x_ticks = ["第{}周".format(i) for i in x]
plt.xticks(x, x_ticks, fontproperties=my_font)
plt.yticks(range(min(y2), max(y2)+1))

plt.xlabel("date")
plt.ylabel("吵架次数", fontproperties=my_font)
plt.title("兔兔鹅不吵架架啦", fontproperties=my_font)

# 多次绘制
plt.plot(x, y1, label="鱼鱼<・)))><<")
plt.plot(x, y2, label="cc")  # 二次plot
         # 还有color、linestyle，linewidth、alpha等参数

plt.grid(alpha=0.4)

# 添加图例
plt.legend(prop=my_font, loc="upper right")
           # 结合label参数显示,加入prop参数修改字体,加入loc参数可修改图例位置

plt.show()
