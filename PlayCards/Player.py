# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-26
    Author: John Huang
'''

class Player:

    def __init__(self, name): 
        self.__name = name 
        self.__remainingCards = []

    def getName(self):
        return self.__name 

    def getCard(self, card): 
        self.__remainingCards.append(card)

    def getAmountOfRemainingCards(self): 
        return len(self.__remainingCards)

    def playCard(self): 
        card = self.__chooseOneCardToPlay() 
        return card

    def __chooseOneCardToPlay(self):
        return self.__remainingCards.pop(0)
