# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-26
    Author: John Huang
'''

SUIT = ['Club', 'Diamond', 'Heart', 'Spade']
VALUE = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Card: 

    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value 

    def __repr__(self): 
        return f'({self.__suit}, {self.__value})'
    
    def __eq__(self, other): 
        return True if self.__suit == other.__suit and self.__value == other.__value else False 

    def __gt__(self, other): 
        if self.isValueGreaterThanOther(other): 
            return True 
        elif self.isValueLessThanOther(other):
            return False 
        elif self.isSuitGreaterThanOther(other):
            return True 
        else: 
            return False  
    
    def __ge__(self, other):
        return True if self.__eq__(other) or self.__gt__(other) else False 

    def isValueGreaterThanOther(self, other):
        return True if VALUE.index(self.__value) > VALUE.index(other.__value) else False 

    def isValueLessThanOther(self, other): 
        return True if VALUE.index(self.__value) < VALUE.index(other.__value) else False 

    def isSuitGreaterThanOther(self, other):
        return True if SUIT.index(self.__suit) > SUIT.index(other.__suit) else False 


