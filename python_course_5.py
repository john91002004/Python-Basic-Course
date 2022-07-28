# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-26
    Author: John Huang
'''

from math import pi, sqrt
import abc

# ========= 2022-07-26 =========== 
# 好的開發程式必須兩個程式
# 1. 產品程式
# 2. 測試程式 - 測試產品的程式

# ========= Geometry 幾何圖形 =========
# 1. 創建各種圖形的類別，繼承自基底類別 Shape 
# 2. 而且基底類別是抽象類別
# 3. Shape裡面有些方法: Area(), Perimeter()

class Shape(abc.ABC): 
    
    @abc.abstractmethod     # @ -> 修飾詞 (Decorator)
    def Area(self):
        pass

    @abc.abstractmethod 
    def Perimeter(self): 
        pass 

class Square(Shape):

    def __init__(self, side): 
        self.side = side

    def Area(self):
        return self.side * self.side

    def Perimeter(self):
        return 4 * self.side 

class Rectangle(Shape):

    def __init__(self, length, width):
        self.width = width 
        self.length = length

    def Area(self):
        return self.length * self.width 

    def Perimeter(self):
        return 2 * (self.width + self.length)

class Circle(Shape): 

    def __init__(self, radius):
        self.radius = radius
    
    def Area(self):
        return pi * self.radius * self.radius

    def Perimeter(self):
        return 2 * pi * self.radius

class Triangle(Shape): 

    def __init__(self, side_A, side_B, side_C): 
        self.side_A = side_A 
        self.side_B = side_B
        self.side_C = side_C 

    def Area(self): # 海龍公式
        s = self.Perimeter() / 2 
        return sqrt( s * (s-self.side_A) * (s-self.side_B) * (s-self.side_C) ) 

    def Perimeter(self):
        return self.side_A + self.side_B + self.side_C
