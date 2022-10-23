import math
import random

class player:

    def __init__(self,letter):
        self.letter=letter;     #x or o

    def get_move(self,game):
        pass   #next move

class RandomComputerPlayer(player):

    def __init__(self,letter):
        super().__init__(letter);

    def get_move(self,game):
        pass

class RandomHumanPlayer(player):

    def __init__(self,letter):
        super().__init__(letter);

    def get_move(self,game):
        pass
    
