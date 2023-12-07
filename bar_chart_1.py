# 假设你获取到了2017年内地电影票房前20的电影(列表a)和电影票房数据(列表b),那么如何更加直观的展示该数据?
# a=[“战狼2”"速度与激情8""功夫瑜伽”,西游伏妖篇","变形金刚5:最后的骑士"."摔跤吧!爸爸”,
# "加勒比海盗5：死无对证”,"金刚:骷髅岛""极限特工: 终极回归","生化危机6:终章”,"乘风破浪”，"神偷奶爸3”,
# "智取威虎山","大闹天竺""金刚狼3:殊死一战","蜘蛛侠英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]
# b=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,
# 10.49,10.3,8.75,7.55,7.32.6.99,6.88,6.86,6.58,6.23]单位:亿
# 数据来源: http://58921.com/alltime/2017

# 条形图

from matplotlib import pyplot as plt
from matplotlib import font_manager

# set the font
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")

# import the data
movie_name = a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5:\n最后的骑士",
                  "摔跤吧!爸爸", "加勒比海盗5:\n死无对证", "金刚:骷髅岛", "极限特工:终极回归",
                  "生化危机6:终章", "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3:殊死一战",
                  "蜘蛛侠英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊"]
box_office = b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12,
                  10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88, 6.86, 6.58, 6.23]

# # check the data size
# print(len(a))
# print(len(b))

# set the picture size
plt.figure(figsize=(13, 9.8), dpi=80)

plt.xticks(range(len(a)), movie_name, rotation=90, fontproperties=my_font)
              # 数字字符串列表对应,x轴刻度信息较长,可以加入换行符

plt.bar(movie_name, box_office, width=0.4)  # 条形宽度

plt.show()
