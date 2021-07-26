# -*- coding = utf-8 -*-
# @Time : 2021-07-23 10:13
# @Author : xs
# @File : testCloud.py
# @Software : PyCharm

import jieba   # 分词
from matplotlib import pyplot as plt    # 绘图，数据可视化
from wordcloud import WordCloud         # 词云
from PIL import Image                   # 图片处理
import numpy as np                      # 矩阵运算
import sqlite3                          # 数据库


# 准备词云所需要的文本
con = sqlite3.connect(r'C:\Users\admin\PycharmProjects\douban_falsk\movie.db')
cur = con.cursor()
sql = 'select instroduction from movie250'
data = cur.execute(sql)
text =""
for item in data:
    text =text +item[0]
# print(text)
cur.close()
con.close()

# 分词
cut = jieba.cut(text)
string = ' '.join(cut)
# print(string)
# print(len(string))  # 统计多少个词

# 绘图
img = Image.open(r'C:\Users\admin\PycharmProjects\douban_falsk\static\assets\img\tree.jpg')
img_array = np.array(img) # 将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='C:\\Windows\\Fonts\\msyh.ttc'   # 字体所在位置 C:\Windows\Fonts

)
wc.generate_from_text(string)

fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')  # 是否显示坐标轴
# plt.show() # 显示生成的词云图
plt.savefig(r"C:\Users\admin\PycharmProjects\douban_falsk\static\assets\img\tree词云图.jpg", dpi = 400) #dpi设置清晰度