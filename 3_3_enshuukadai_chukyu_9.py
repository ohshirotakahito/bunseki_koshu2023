# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:50:24 2023

@author: toshiro
"""
#9.欠損値の補完:

import pandas as pd
import numpy as np

# データセット
data = pd.DataFrame({'A': [12, np.nan, 34, 56], 'B': [45, 67, np.nan, 78]})

# 補完前のデータを表示
print(data)

# 欠損値を列の平均値で補完
imputed_data = data.fillna(data.mean())

# 補完後のデータを表示
print(imputed_data)
