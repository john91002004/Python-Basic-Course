# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-28
    Author: John Huang
'''

from Card import Card, SUIT, VALUE

class Deck: 

    def __init__(self): 
        self.__createFiftyTwoCards() 

    def getAmountOfRemainingCards(self): 
        return len(self.__remainingCards)

    def __createFiftyTwoCards(self):
        self.__remainingCards = [] 
        for value in VALUE:
            for suit in SUIT:
                self.__remainingCards.append( Card(suit, value) )
        self.__remainingCards.reverse() 

    def getFirstCard(self):
        if len(self.__remainingCards) == 0: 
            return None
        else: 
            return self.__remainingCards.pop(0)




