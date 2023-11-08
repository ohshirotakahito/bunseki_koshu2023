# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:50:24 2023

@author: toshiro
"""
#１３．基本的な画像処理:

import cv2
import matplotlib.pyplot as plt

# 画像の読み込み
image = cv2.imread('data/tex_image.png')

# 元の画像を表示
cv2.imshow('Original Image', image)
cv2.waitKey(0)  # キーボード入力があるまでウィンドウを表示

# カラー画像をグレースケールに変換
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# グレースケール画像を表示
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)  # キーボード入力があるまでウィンドウを表示

# ヒストグラムの作成
plt.hist(gray_image.ravel(), bins=256, range=[0,256], fc='k', ec='k')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram of Grayscale Image')
plt.show()