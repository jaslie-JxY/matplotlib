# 假设通过爬虫你获取到了北京2016年3,10月份每天的最高气温(分别位于列表a,b),
# 那么此时如何寻找出气温随时间(天)变化的某种规律?
# a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
# b = [26,26,28,19,21,17,1,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
# 数据来源: http://lishi.tianai.com/beiing/index.html

# 绘制散点图

from matplotlib import pyplot as plt
from matplotlib import font_manager

# change the font
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")

# import the data
x_3 = date_3 = range(1, 32)
x_10 = date_10 = range(41, 72)
y_3 = temp_3 = a = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14,
                    17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22, 23]
y_10 = temp_10 = b = [26, 26, 28, 19, 21, 17, 1, 19, 18, 20, 20, 19, 22, 23,
                      17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13, 12, 13, 6]

# set the picture size
plt.figure(figsize=(15.7, 9), dpi=80)

# adjust the axis scale
_x = list(x_3) + list(x_10)
x_ticks = ["3月{}号".format(i) for i in x_3]
x_ticks += ["10月{}号".format(i-50) for i in x_10]
plt.xticks(_x[::3], x_ticks[::3], rotation=45, fontproperties=my_font)

# add description
plt.xlabel("date")
plt.ylabel("temperature")
plt.title("气温时间变化规律图", fontproperties=my_font)

# 使用scatter方法绘制散点图
plt.scatter(x_3, y_3, label="3月")
plt.scatter(x_10, y_10, label="10月")

plt.grid(alpha=0.4)

plt.legend(prop=my_font)

plt.show()
