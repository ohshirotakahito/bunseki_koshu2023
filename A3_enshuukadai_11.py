# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:46:31 2023

@author: ohshi
"""

#本のクラス:
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
    
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}")

# 5冊の本のインスタンスを作成
book1 = Book("1984", "George Orwell", "Dystopian")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Classic")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Novel")
book4 = Book("One Hundred Years of Solitude", "Gabriel García Márquez", "Magical Realism")
book5 = Book("Pride and Prejudice", "Jane Austen", "Romance")

# 各本の情報を表示
book1.display_info()
book2.display_info()
book3.display_info()
book4.display_info()
book5.display_info()


#動物園の動物クラス:
class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Species: {self.species}, Name: {self.name}, Age: {self.age}")

# 動物のインスタンスを作成
elephant = Animal("Elephant", "Dumbo", 10)
lion = Animal("Lion", "Simba", 5)
monkey = Animal("Monkey", "George", 3)

# 各動物の情報を表示
elephant.display_info()
lion.display_info()
monkey.display_info()


#学生のクラス:
class Student:
    def __init__(self, name, grade, major):
        self.name = name
        self.grade = grade
        self.major = major
    
    def display_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}, Major: {self.major}")

#クラスのインスタンス化          
student1 = Student("Taro Yamada", "Sophomore", "Computer Science")
#学生情報の表示
student1.display_info()


#カレンダーのクラス
class Calendar:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def is_leap_year(self):
        # 閏年かどうかを判定
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)
    
    def get_days_in_month(self):
        # 各月の日数を定義
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # 2月の場合、閏年かどうかをチェック
        if self.month == 2:
            return 29 if self.is_leap_year() else 28
        # それ以外の月の日数を返す
        return month_days[self.month - 1]

#クラスのインスタンス化    
my_calendar = Calendar(2023, 4)  # 2023年4月のカレンダー
#月の日数の取得
days_in_month = my_calendar.get_days_in_month()
print(f"{my_calendar.month}月は{days_in_month}日あります。")


#ショッピングカートのクラス
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def calculate_total(self):
        return sum(self.items)

#クラスのインスタンス化
my_cart = ShoppingCart()
# 商品の価格を追加
my_cart.add_item(100)  # 100円の商品
my_cart.add_item(200)  # 200円の商品
#合計金額の計算
total = my_cart.calculate_total()
print("Total amount:", total)  # 合計金額を表示
 


#天気のクラス
class Weather:
    def __init__(self, high, low):
        self.high = high
        self.low = low
    
    def get_average_temperature(self):
        return (self.high + self.low) / 2

#クラスのインスタンス化
today_weather = Weather(30, 20)  # 最高気温30度、最低気温20度
#平均気温の取得
average_temp = today_weather.get_average_temperature()
print("Average Temperature:", average_temp)


#時間のクラス
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def display_time(self):
        print(f"{self.hour}:{self.minute}:{self.second}")

#クラスのインスタンス化
current_time = Time(9, 30, 45)
#時間の表示
current_time.display_time()


#電卓のクラス
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        return self.a / self.b if self.b != 0 else None

#クラスのインスタンス化
calc = Calculator(10, 5)
#加算
result = calc.add()
print("Addition:", result)  # 15 (10 + 5)
#減算
result = calc.subtract()
print("Subtraction:", result)  # 5 (10 - 5)
#乗算
result = calc.multiply()
print("Multiplication:", result)  # 50 (10 * 5)
#除算
result = calc.divide()
print("Division:", result)  # 2 (10 / 5)


#電車のスケジュールクラス
class TrainSchedule:
    def __init__(self, schedule):
        self.schedule = schedule
    
    def find_trains(self, time):
        # ここに時刻に基づいて電車を検索するコードを記述
        pass

# スケジュールの例
schedule = {'08:00': 'Train A', '09:00': 'Train B', '10:00': 'Train C'}
#クラスのインスタンス化
train_schedule = TrainSchedule(schedule)
# 特定の時刻で利用可能な電車を検索
available_train = train_schedule.find_trains('09:00')
print(available_train)


#レシピのクラス
class Recipe:
    def __init__(self, ingredients, steps):
        self.ingredients = ingredients
        self.steps = steps
    
    def display_recipe(self):
        print("Ingredients:", self.ingredients)
        print("Steps:", self.steps)

# レシピの例
ingredients = ["2 eggs", "1 cup sugar", "1 cup flour"]
steps = ["Beat eggs", "Add sugar", "Mix with flour", "Bake for 20 minutes at 180°C"]
#クラスのインスタンス化
my_recipe = Recipe(ingredients, steps)
#レシピの表示
my_recipe.display_recipe()
