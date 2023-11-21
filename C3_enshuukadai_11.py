# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:52:40 2023

@author: ohshi
"""
# =============================================================================
# １１．液体クロマトグラフィーデータに基づく保持時間の予測モデル作成
# 背景
# 液体クロマトグラフィーは、化学物質の分離と同定に広く用いられる技術です。この演習では、液体クロマトグラフィーにおける化学物質の保持時間を予測する機械学習モデルを作成し、評価します。
# 
# データセット
# 提供されるデータセットには、以下のカラムが含まれます：
# 
# 保持時間（分）
# ファンデルワールス半径（pm）
# HOMO エネルギー（eV）
# LUMO エネルギー（eV）
# 酸化還元電位（V）
# 分子量（g/mol）
# 分極率
# pKa
# ベンゼン環の数
# 課題
# データセットを読み込み、適切に前処理を行ってください。
# 保持時間を目的変数とし、他の特徴量を用いて機械学習モデルを作成してください。モデルの種類は任意です（例：線形回帰、ランダムフォレスト、勾配ブースティングなど）。
# モデルをトレーニングデータで訓練し、テストデータで評価してください。評価指標として、少なくとも平均二乗誤差（MSE）と決定係数（R²）を報告してください。
# 実際の保持時間と予測された保持時間をプロットし、モデルの予測性能を視覚的に評価してください。
# 追加のチャレンジ（オプション）
# 異なる機械学習モデルを試し、それらの性能を比較してください。
# モデルの過学習または適切な学習を確認するために、交差検証を実施してください。
# 特徴量の重要度を評価し、どの特徴量が保持時間の予測に最も寄与しているかを分析してください。
# 
# =============================================================================


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import matplotlib.pyplot as plt

# Loading the provided dataset
file_path = 'data/liquid_chromatography_data.csv'
data = pd.read_csv(file_path)

# Separating the target variable (Retention Time) and features
X = data.drop('Retention Time (min)', axis=1)
y = data['Retention Time (min)']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Creating and training the RandomForestRegressor model
regressor = RandomForestRegressor(n_estimators=100, random_state=42)
regressor.fit(X_train, y_train)

# Predicting on the test set
y_pred = regressor.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('MSE:', mse, 'R2:', r2)

# Plotting predicted vs actual retention times
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)  # Diagonal line
plt.xlabel('Actual Retention Time (min)')
plt.ylabel('Predicted Retention Time (min)')
plt.title('Actual vs Predicted Retention Times')
plt.grid(True)
plt.show()