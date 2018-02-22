# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:55:14 2018

@author: peter
"""

import numpy as np
import random
from matplotlib import pyplot as plt

#生产随机数列，一共2组，每组100个随机数
x1 = np.random.random(100) + 2.2
x2 = np.random.random(100) + 2.9
y1 = np.random.random(100) + 2.2
y2 = np.random.random(100) + 2.9

#cp1 = [[i, j, 'red'] for (i, j) in zip(x1, y1)]
#cp2 = [[i, j, 'blue'] for (i, j) in zip(x2, y2)]
cp1 = [[i, j] for (i, j) in zip(x1, y1)]
cp2 = [[i, j] for (i, j) in zip(x2, y2)]
#把2组数列合成并打乱
cp = cp1 + cp2
cp = np.array(cp)
np.random.shuffle(cp)

#显示生成的数列
plt.scatter(cp[:, 0], cp[:, 1])#c=cp[:, 2]
plt.show()


#随机选取任意2点作为每组的“质心”（因为我只要分2组，如果要分N组，就随机取N点）
p1 = random.choice(cp)
p2 = random.choice(cp)

#主循环开始
for repeat in range(len(cp) // 2):
    #新建2个空序列
    c1 = []
    c2 = []
    #对序列中的每一点求到2个“质心”的距离，比较离那个质心近就归到那个组
    for i in range(len(cp)):
        d1 = np.power((float(cp[i][0]) - float(p1[0])), 2) + \
            np.power((float(cp[i][1]) - float(p1[1])), 2)
        d2 = np.power((float(cp[i][0]) - float(p2[0])), 2) + \
            np.power((float(cp[i][1]) - float(p2[1])), 2)
        if d1 < d2:
            c1.append(cp[i])
        else:
            c2.append(cp[i])

    #对分好组以后的序列重新求每组的“质心”，方法是求每组中所有点的x和y的坐标的平均值
    z1x, z1y = 0, 0
    for e in c1:
        z1x += float(e[0])
        z1y += float(e[1])
    p1x = z1x * 1.0 / len(c1)
    p1y = z1y * 1.0 / len(c1)
    p1 = np.array([p1x, p1y])

    z2x, z2y = 0, 0
    for e in c2:
        z2x += float(e[0])
        z2y += float(e[1])
    p2x = z2x * 1.0 / len(c2)
    p2y = z2y * 1.0 / len(c2)
    p2 = np.array([p2x, p2y])

    #把这2组转化为numpy数列
    c1 = np.array(c1)
    c2 = np.array(c2)

#显示分类后的结果
plt.scatter([float(i) for i in c1[:, 0]], [float(j)
                                           for j in c1[:, 1]], c='red')
plt.scatter([float(i) for i in c2[:, 0]], [float(j)
                                           for j in c2[:, 1]], c='blue')
plt.show()
