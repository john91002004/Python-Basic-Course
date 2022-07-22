# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-19
    Author: John Huang
'''

# ========= 2022-07-22 =========== 

# 物件導向3大特色: (Object-Oriented)
# 1. 封裝 (Encapsulation)
# 2. 繼承 (Inheritage)
# 3. 多型 (Polymorphism)

# 封裝: Class 型別展示 
# 類別裡的變數(variable) -> 屬性(attribute), 類別裡的函式(function) -> 方法(method)
# 屬性和方法都叫做該類別的成員(member)
# 成員前綴符號 __ 即為私有成員(private member)，例如 __hahaha()
# 一般成員則為公有成員(public member)
class Person: 
    def __init__(self, name, gender, birthday):
        self.__Name = name  
        self.__Gender = gender 
        self.__Birthday = birthday

    def introduceMyname(self):
        return self.__Name 

    def introduceMyself(self):
        print(f'My name is {self.__Name}.')
        print(f'I am a {self.__Gender}.')
        print(f'I was born in {self.__Birthday}')

# 繼承: 實作Student型別
# Student為子類別，繼承的父類別是Person。
# 除非覆載(override)，否則保有父類別所有的成員。
class Student(Person): 
    def __init__(self, name, gender, birthday, studentID):
        self.studentID = studentID 
        super().__init__(name, gender, birthday)

    def introduceMyself(self):
        super().introduceMyself()
        print(f'My studentID is {self.studentID}')


# 多型: 實作complex型別
# __init__(), __repr__(), __str__() 覆載掉原本繼承的基底型別(物件型別)  (override)
class complex2:
    def __init__(self, real, imag):     # 建構子 (constructor) <-相對概念-> 解構子 (destructor)
        self.real = real 
        self.imag = imag 
    
    def __repr__(self):     # 表示 (representation)
        if self.imag < 0 : 
            return f'{self.real} - {-self.imag}j'
        else : 
            return f'{self.real} + {self.imag}j'

    def __str__(self):      # 字串 (string)
        return self.__repr__()

    def conjugate(self): 
        return complex2(self.real, -self.imag)

# 出題1: 用自訂義類別實作堆疊(Stack)
# 原則: 後進先出(Last In First Out, LIFO)
# 1. 調用push函式時，將參數放到資料結構裡
# 2. 調用pop函式時，將資料結構裡最"後"放入的參數取出




# 出題2: 用自訂義類別實作佇列(Queue)
# 原則: 先進先出(First In First Out, FIFO)
# 1. 調用push函式時，將參數放到資料結構裡
# 2. 調用pop函式時，將資料結構裡最"先"放入的參數取出


