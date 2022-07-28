# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-28
    Author: John Huang
'''

import unittest

from Deck import Deck

class DeckTest(unittest.TestCase):

    def setUp(self) -> None:
        self.deck = Deck()
        return super().setUp()

    def testFiftyTwoCards(self): 
        self.assertEqual( self.deck.getAmountOfRemainingCards(), 52) 

    def testNoDuplicate(self):
        FirstCard = self.deck.getFirstCard() 
        while True: 
            SecondCard = self.deck.getFirstCard()
            if SecondCard == None: 
                break 
            self.assertGreater(FirstCard, SecondCard)
            FirstCard = SecondCard

if __name__ == '__main__': 
    unittest.main(verbosity=4)
