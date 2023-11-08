# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 01:23:04 2023

@author: toshiro
"""
#１． 画像解析:

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure

# 画像ファイルの読み込み
image = cv2.imread('data/particle_image.png', cv2.IMREAD_GRAYSCALE)

# 画像を二値化
threshold_value = 128  # 閾値を調整する必要があるかもしれません
binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)[1]

# 連結成分をラベル付け
labels = measure.label(binary_image, connectivity=2)

# 各ラベル領域のプロパティを計算
regions = measure.regionprops(labels)

# 粒子のサイズと形状情報を格納するリスト
particle_sizes = []
particle_shapes = []

# 各ラベル領域のサイズと形状情報を取得
for region in regions:
    # 面積を取得して粒子サイズとして記録
    particle_size = region.area
    particle_sizes.append(particle_size)

    # 形状情報（例: 矩形のアスペクト比）を取得して記録
    min_row, min_col, max_row, max_col = region.bbox
    height = max_row - min_row
    width = max_col - min_col
    aspect_ratio = width / height
    particle_shapes.append(aspect_ratio)

# 粒子サイズ分布をプロット
plt.hist(particle_sizes, bins=20, range=(0, max(particle_sizes)))
plt.xlabel('Particle Size')
plt.ylabel('Frequency')
plt.title('Particle Size Distribution')
plt.show()

# 粒子形状情報をプロット
plt.hist(particle_shapes, bins=20, range=(0, max(particle_shapes)))
plt.xlabel('Aspect Ratio')
plt.ylabel('Frequency')
plt.title('Particle Shape Distribution')
plt.show()
