# 在美国2004年人口普查发现有许多人在离家相对较远的地方工作。
# 根据他们从家到上班地点所需要的时间,通过抽样统计(最后一列)出了下表的数据这些数据能够绘制成直方图么?

# 处理过的数据，组距不等的直方图

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")

# import the processed data
interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90, 150]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]

# print(sum(quantity))
# print(len(interval), len(width), len(quantity))

plt.figure(figsize=(13.7, 7.7), dpi=80)

x_ticks = [i-0.5 for i in range(len(quantity)+1)]
plt.xticks(x_ticks, interval)

plt.bar(range(len(quantity)), quantity, width=1)
        # 使用bar方法绘制条形图，设置宽度为1模拟直方图

plt.xlabel("家到上班地点的时间(min)", fontproperties=my_font)
plt.ylabel("quantity")

plt.grid(alpha=0.4)

plt.show()
