# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#2.棒グラフの作成:

import matplotlib.pyplot as plt
# データ
data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

# 箱ひげ図
plt.boxplot(data)
plt.show()

