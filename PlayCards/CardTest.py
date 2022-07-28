# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-26
    Author: John Huang
'''

import unittest

from Card import Card

class CardTest(unittest.TestCase): 

    def testEqual(self): 
        self.assertEqual( Card('Spade', 'A'), Card('Spade', 'A') )
        
    def testGreaterOrEqual(self):
        self.assertGreater( Card('Spade', 'A') , Card('Diamond', 'A') )
        self.assertGreater( Card('Heart', '10'), Card('Heart', '9') )
        self.assertGreaterEqual(Card('Diamond', 'A') , Card('Diamond', 'A'))

    def testLessOrEqual(self): 
        self.assertLess( Card('Club', '2'), Card('Diamond', '2') )
        self.assertLess( Card('Heart', '2'), Card('Diamond', 'K') )
        self.assertLessEqual(Card('Diamond', 'K'), Card('Diamond', 'K'))

if __name__ == '__main__': 
    unittest.main(verbosity=4)
