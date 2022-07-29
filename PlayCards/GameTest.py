# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-29
    Author: John Huang
'''

import unittest 

class GameTest(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game('John', 'Jenny', 'Jones', 'Jan')
        return super().setUp()

    def testCallPlayersPlayCard(self):
        self.game.callPlayersPlayCard() 
        self.assertEqual( self.game.getCardsOfThisRound(), 4) 







if __name__ == '__main__': 
    unittest.main(verbosity=4)
