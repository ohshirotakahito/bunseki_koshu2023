# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:09:27 2023

@author: toshiro
"""
a = 10
b = 20.5

#変数の定義
print(a,b)

c = "Hello, World!"
print(c)

#基本的なデータ型
print(type(c))

#演算子
print(a + b, a - b, a * b, a / b)

#条件分岐
if a >= 10:
    print("a is 10 or more")
else:
    print("a is less than 10")
    
#ループ
for i in range(1, 11):
    print(i)

#リスト
d = [1, 2, 3, 4, 5]
print(d)

#リストの操作
d.append(6)
print(d)

#文字列の操作
c_upper = c.upper()
print(c_upper)

#関数の定義
def sum_two_numbers(num1, num2):
    return num1 + num2

#関数の呼び出し
sum_result = sum_two_numbers(10, 20)
print(sum_result)

