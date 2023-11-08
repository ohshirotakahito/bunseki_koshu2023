# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:50:24 2023

@author: toshiro
"""
#１２．データのグルーピングと集計:

import pandas as pd

# データセットの定義
data = pd.DataFrame({'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 'Age': [23, 45, 34, 30, 25]})

# 'Gender'列でデータをグルーピングし、各グループの'Age'の平均値を計算
grouped_data = data.groupby('Gender').mean()

# 結果を表示
print(grouped_data)