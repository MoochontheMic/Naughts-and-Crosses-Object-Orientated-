from ..Board import Board
from ..Player import Player
from  ..game import Game

class TestGame():

    def testWinStatements(self):
        """
        Tests the game prints the correct statements on win
        """
        board = Board()
        player = Player()
        game = Game()
        game.currentPlayerX = True
        board.cells = [['X', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        board.updatecell([3,1],'X')
        
        board

