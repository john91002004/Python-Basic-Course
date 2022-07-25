# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-22
    Author: John Huang
'''

import unittest
from python_homework_2 import Stack, Stack2 

# ========= 2022-07-25 =========== 
# 1. 必須創建一個新類別，作為測試的地方，必且該類別必須繼承unittest.TestCase。
# 2. assert是斷言的意思。
# 3. 每一個函式的開頭必須使用test，才會被當作要測試的Case。
# 4. 使用終端機下指令: py .\name.py 進行測試 
# 5. OK表示測試通過，FAILED表示測試沒通過。
#    沒通過的原因有兩種: FAIL -> 斷言失敗, ERROR -> 程式碼有錯誤

class SimpleTest(unittest.TestCase):
    
    def testOneEqualsOne(self):
        self.assertEqual(1, 1)          # OK

    def testTwoGreaterThanOne(self):
        self.assertGreater(1, 1)        # FAIL

    def testIfZeroEqualsZero(self):
        self.assertF()                  # ERROR


# =========== Test Stack ==========
# 1. 盡量包含所有應該測試的Case。
# 2. Case要表現的是函式的行為，所以應當從函式的行為去建構測試。

class StackTest(unittest.TestCase):

    def setUp(self) -> None:
        s = Stack()                 #   區域變數s 只能在該函式中使用
        self.s = Stack2()            #   成員變數self.s 可以在該類別中的任意地方使用
        return super().setUp()

    def testPushOneElementAndPop(self): 
        self.s.push(1)
        result = self.s.pop() 
        self.assertEqual(result, 1)

    def testPushTenElementsAndPopOne(self): 
        for i in range(10): 
            self.s.push(i)
        result = self.s.pop() 
        self.assertEqual(result, 9)

    def testPushTenElementsAndPopTen(self):
        for i in range(10):
            self.s.push(i)
        for i in range(9, -1, -1):
            with self.subTest(i=i):         # subTest的用法，可以更好的知道迴圈甚麼地方錯了。
                result = self.s.pop()
                self.assertEqual(result, i)

    def testPopFromEmptyStack(self):
        with self.assertRaises(IndexError):
            self.s.pop() 


if __name__ == '__main__': 
    unittest.main(verbosity=4)
