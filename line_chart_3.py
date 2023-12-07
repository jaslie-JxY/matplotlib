# 根据自己的实际情况,统计出来了最近20周和对象吵架的次数如列表a,请绘制出该数据的折线图
# 以便分析自己每年和对象吵架的数量走势a = [1,0,2,1,3,1,2,1,3,1,0,2,3,2,1,1,0,1,0,1]
# 要求: y轴表示吵架次数 x轴表示周数,比如第1周,第2周等

from matplotlib import pyplot as plt
from matplotlib import font_manager  # 导入修改字体模块

# 修改字体
my_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\msyh.ttc")

# 导入数据
x = range(1, 21)
y = a = [1, 0, 2, 1, 3, 1, 2, 1, 3, 1, 0, 2, 3, 2, 1, 1, 0, 1, 0, 1]

# 调整图片大小
plt.figure(figsize=(17, 7.7), dpi=80)

# 调整坐标轴刻度
x_ticks = ["第{}周".format(i) for i in x]
plt.xticks(x, x_ticks, fontproperties=my_font)  # 列表对应
# plt.yticks(y)  # 刻度值,网格线变粗
plt.yticks(range(min(y), max(y)+1))

# 添加描述信息
plt.xlabel("date")
plt.ylabel("吵架次数", fontproperties=my_font)
plt.title("兔宝，好啦，我们不吵啦", fontproperties=my_font)

# 画图
plt.plot(x, y)

# 绘制网格
plt.grid(alpha=0.4)  # 透明度0-1

# 展示
plt.show()
