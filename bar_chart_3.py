# 假设你知道了列表a中电影分别在2017-09-14(b_14)2017-09-15(b_15)2017-09-16(b_16)三天的票房,
# 为了展示列表中电影本身的票房以及同其他电影的数据对比情况,应该如何更加直观的呈现该数据?
# a=[”猩球崛起3:终极之战”,"敦刻尔克”,"蜘蛛侠:英雄归来”,“战狼2”]
# b_16 =[15746,312,4497,319]
# b_15=[12357,156,2045,1681]
# b_14 =[2358,399,2358,3621]
# 数据来源: http://www.cbooo.cn/moviedav

# 绘制多次条形图

from matplotlib import pyplot as plt
from matplotlib import font_manager

# set the font
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")

# import the data
movie_name = a = ["猩球崛起3:终极之战", "敦刻尔克", "蜘蛛侠:英雄归来", "战狼2"]
box_office_14 = b_14 = [2358, 399, 2358, 3621]
box_office_15 = b_15 = [12357, 156, 2045, 1681]
box_office_16 = b_16 = [15746, 312, 4497, 319]

# set the picture size
plt.figure(figsize=(13.7, 7), dpi=80)

bar_width = 0.3

# 创建横轴数字列表
x_14 = range(len(a))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width for i in x_15]  # 坐标偏移一个width的距离

# adjust the axis scale
plt.xticks(fontproperties=my_font)  # 坐标轴显示中文
plt.xticks(x_15, a)  # 将数字列表对应成坐标中文显示

# add description
plt.ylabel("票房", fontproperties=my_font)

plt.bar(x_14, box_office_14, width=bar_width, color="orange", label="九月十四")
plt.bar(x_15, box_office_15, width=bar_width, label="九月十五")
plt.bar(x_16, box_office_16, width=bar_width, color="purple", label="九月十六")
         # 利用数字列表和纵轴数据对应作图

# add legend
plt.legend(prop=my_font)
    # legend方法结合label参数添加图例
plt.show()
