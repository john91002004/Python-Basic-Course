# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-22
    Author: John Huang
'''

# 出題1: 用自訂義類別實作堆疊(Stack)
# 原則: 後進先出(Last In First Out, LIFO)
# 1. 調用push函式時，將參數放到資料結構裡
# 2. 調用pop函式時，將資料結構裡最"後"放入的參數取出

class Stack:

    def __init__(self): 
        self.__stack = [] 
        self.__pointer = 0 
    
    def push(self, element): 
        self.__stack.append(element)
        self.__pointer += 1 

    def pop(self): 
        try:
            self.__pointer -= 1
            result = self.__stack[self.__pointer]
            self.__stack = self.__stack[0:-1]
            return result
        except:
            print('已經空了！你還在pop什麼？以為自己很厲害？')

# 或者，直接調用list內建函式
class Stack2: 

    def __init__(self): 
        self.__stack = [] 
    
    def push(self, element): 
        self.__stack.append(element)

    def pop(self): 
        return self.__stack.pop() 


# 出題2: 用自訂義類別實作佇列(Queue)
# 原則: 先進先出(First In First Out, FIFO)
# 1. 調用push函式時，將參數放到資料結構裡
# 2. 調用pop函式時，將資料結構裡最"先"放入的參數取出

class Queue():

    def __init__(self): 
        self.__queue = [] 
    
    def push(self, element):
        self.__queue.append(element)

    def pop(self): 
        result = self.__queue[0]
        self.__queue = self.__queue[1:]
        return result 

# 或者，直接用list內建的函式
class Queue2():
    
    def __init__(self): 
        self.__queue = [] 
    
    def push(self, element):
        self.__queue.append(element)

    def pop(self): 
        return self.__queue.pop(0)
    