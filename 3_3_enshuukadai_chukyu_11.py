# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:50:24 2023

@author: toshiro
"""
#11. 複数のデータセットの結合:

import pandas as pd

# データセットの定義
data1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
data2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})

# 複数のデータセットの結合
combined_data = pd.concat([data1, data2], axis=1)

# 結合したデータを表示
print(combined_data)
