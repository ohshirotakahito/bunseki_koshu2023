# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 01:10:58 2023

@author: toshiro
"""
#１４．画像解析:

import cv2
import matplotlib.pyplot as plt

# 画像を読み込む
image = cv2.imread('data/cell_microscope_image.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 元画像を表示
plt.figure(figsize=(10,10))
plt.imshow(image_rgb)

# 色の閾値に基づいてセグメンテーションを行う
# 青（核）の領域を抽出
mask_blue = cv2.inRange(image_rgb, (50, 0, 50), (255, 100, 255))
blue_area = cv2.bitwise_and(image_rgb, image_rgb, mask=mask_blue)

# 緑（細胞内小胞体）の領域を抽出
mask_green = cv2.inRange(image_rgb, (0, 50, 0), (100, 255, 100))
green_area = cv2.bitwise_and(image_rgb, image_rgb, mask=mask_green)

# 赤（細胞骨格）の領域を抽出
mask_red = cv2.inRange(image_rgb, (50, 0, 0), (255, 100, 100))
red_area = cv2.bitwise_and(image_rgb, image_rgb, mask=mask_red)

# 各領域の割合を計算
total_pixels = image_rgb.shape[0] * image_rgb.shape[1]
blue_ratio = (mask_blue > 0).sum() / total_pixels
green_ratio = (mask_green > 0).sum() / total_pixels
red_ratio = (mask_red > 0).sum() / total_pixels

# 各領域の割合の表示
print(blue_ratio, green_ratio, red_ratio)

# ラベリングされた画像を作成
labeled_image = image_rgb.copy()

# 各色の領域をラベリング
labeled_image[mask_blue > 0] = [0, 0, 255]  # 青色領域
labeled_image[mask_green > 0] = [0, 255, 0]  # 緑色領域
labeled_image[mask_red > 0] = [255, 0, 0]  # 赤色領域

# ラベリングされた画像を表示
plt.figure(figsize=(10,10))
plt.imshow(labeled_image)
plt.axis('off')
plt.title('Labeled Image')
plt.show()
