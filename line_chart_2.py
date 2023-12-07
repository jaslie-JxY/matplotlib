# 如果列表a表示10点到12点的每一分钟的气温,如何绘制折线图观察每分钟气温的变化情况?
# a=[random.randint(20,35) for i in range(120)]

# 导入模块
from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

# 设置支持中文显示的字体
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")

# 导入数据
x = time = range(1, 121)
y = temp = a = [random.randint(20, 35) for i in range(120)]

# 设置图片大小
plt.figure(figsize=(8.7, 5.7), dpi=80)

# 调整坐标轴刻度
x_ticks = ["10点{}分".format(i) for i in range(60)]
x_ticks += ["11点{}分".format(i) for i in range(60)]
plt.xticks(x[::10], x_ticks[::10], rotation=45, fontproperties=my_font)
                  # 数字列表与字符串列表对应,rotation-逆时针旋转角度,加入fontproperties参数修改字体

# 画图
plt.plot(time, temp)

# 添加描述信息
plt.xlabel("time")
plt.ylabel("temperature")
plt.title("10-12点的气温", fontproperties=my_font)

# # 保存
# plt.savefig(".\\figure_2.png")  # 与转义符反斜杠'\'区分
# plt.savefig("D:/ucas/figure_2.svg")

# 展示
plt.show()
