# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#9. Seabornを使ったデータの可視化:

import seaborn as sns
import matplotlib.pyplot as plt

# データ
data = sns.load_dataset('titanic')

# ペアプロット
sns.pairplot(data)
plt.show()
