# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:50:24 2023

@author: toshiro
"""
#7. 階層的クラスタリング:

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# データセット
data = [[2.5, 3.4], [3.6, 4.5], [2.9, 3.9], [4.2, 5.1], [3.1, 3.7]]

# 階層的クラスタリングの実行
Z = linkage(data, 'ward')

# デンドログラムの作成
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title('Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Euclidean Distances')
plt.show()

# デンドログラムを解釈してクラスター数を決定する（例えば、クラスター数を3とする）
num_clusters = 3

