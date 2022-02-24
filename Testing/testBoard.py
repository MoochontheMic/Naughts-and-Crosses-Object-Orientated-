from Player import Player
from ..Board import Board

class TestBoard():
    
    def testUpdateCell(self):
        """
        Test updating a cell
        """
        board = Board()
        print('\n')
        board.display()
        board.updatecell([2, 1], Player('X'))
        print('\n')
        board.display()
