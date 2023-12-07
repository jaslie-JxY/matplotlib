# 假设一天中每隔两个小时(range(2,26,2))的气温(C)分别是[15,13,14.5,17,20,25,26,26,27,22,18,15]
# 绘制折线图
# ctrl+click进入源码
# ctrl+l注释
# ctrl+alt+l自动格式化代码

# 导入模块
from matplotlib import pyplot as plt

# 导入数据
x = time = range(2, 26, 2)  # range(start,stop,step)取不到stop值
y = temp = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

# 设置图片大小
plt.figure(figsize=(7, 4.7), dpi=80)  # figsize=(width,height)_in_inches dots-per-inch

# 设置坐标轴刻度
plt.xticks(x)
y_ticks = range(min(y), max(y)+1)
plt.yticks(y_ticks[::2])  # 列表太密集取步长

# 画图
plt.plot(time, temp)

# # 保存
# plt.savefig(".\\figure_1.png")  # 保存到当前路径
# plt.savefig("D:\\ucas\\figure.svg")  # 指定路径，文件名及格式(\\or/)

# 展示
plt.show()
