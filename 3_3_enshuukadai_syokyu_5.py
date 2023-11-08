# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 02:22:01 2023

@author: toshiro
"""
# 初期のデータ
C1 = 0.05  # mol/L
V1 = 10  # ml

# 新しい溶液のボリューム
V2 = V1 + 50  # 10mlの初溶液 + 50mlの脱イオン水

# 新しい溶液のモル濃度の計算
C2 = (C1 * V1) / V2

print(C2)
