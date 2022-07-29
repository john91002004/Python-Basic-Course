# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-28
    Author: John Huang
'''

import unittest

from Deck import Deck, NoSuchCardException
from Card import Card

class DeckTest(unittest.TestCase):

    def setUp(self) -> None:
        self.deck = Deck()
        return super().setUp()

    def testFiftyTwoCards(self): 
        self.assertEqual( self.deck.getAmountOfRemainingCards(), 52) 

    # 用的方法是檢查從大到小的排列，只要前一張大於後一張，就保證所有的卡片沒有重複
    def testNoDuplicate(self):
        FirstCard = self.deck.getFirstCard() 
        while True: 
            SecondCard = self.deck.getFirstCard()
            if SecondCard == None: 
                break 
            self.assertGreater(FirstCard, SecondCard)
            FirstCard = SecondCard

    def testNoSuchCardLeftInDeckIfDistributeOneCard(self): 
        card = Card('Spade', 'A')
        self.deck.distributeCards(card)
        self.assertEqual( self.deck.getAmountOfRemainingCards(), 51) 
        with self.assertRaises(NoSuchCardException):
            self.deck.distributeCards(card)

    def testNoCardLeftIfDistributeAllCards(self): 
        sampleDeck = Deck()
        for i in range(52): 
            card = sampleDeck.getFirstCard()
            self.deck.distributeCards(card)
        self.assertEqual( self.deck.getAmountOfRemainingCards(), 0)




if __name__ == '__main__': 
    unittest.main(verbosity=4)
