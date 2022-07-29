# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-26
    Author: John Huang
'''

class Game:

    def __init__(self, playerA, playerB, playerC, playerD): 
        self.playerA = Player(playerA)
        self.playerB = Player(playerB)
        self.playerC = Player(playerC)
        self.playerD = Player(playerD)

