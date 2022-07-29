# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-29
    Author: John Huang
'''

import unittest 
from Card import Card
from Player import Player 

class PlayerTest(unittest.TestCase): 

    def setUp(self) -> None:
        self.player = Player('John')
        card = Card('Spade', 'A')
        self.player.getCard(card)
        return super().setUp()

    def testGetCard(self): 
        self.assertEqual( self.player.getAmountOfRemainingCards(), 1 )

    def testPlayCard(self): 
        cardPlayed = self.player.playCard()
        self.assertEqual( cardPlayed, Card('Spade', 'A') )
        self.assertEqual( self.player.getAmountOfRemainingCards(), 0)



if __name__ == '__main__': 
    unittest.main(verbosity=4)
