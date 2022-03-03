import pytest
from Player import Player
from ..Board import Board

class TestBoard():
    
    # def gameVisualiser(self):
    #     """
    #     Test updating a cell
    #     """
    #     board = Board()
    #     print('\n')
    #     board.display()
    #     board.updatecell([2, 1], Player('X'))
    #     print('\n')
    #     board.display()

    # def testBoardReset(self):
    #     board = Board()
    #     player = Player('X')
    #     moveCoordinate = [0,0]
    #     board.updatecell(moveCoordinate, player=player)
    #     board.resetBoard()

    #     assert board.cells == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    #     assert moveCoordinate in player.positions

    # def testInvalidMove(self, capsys):
    #     board = Board()
    #     player = Player('X')

    #     board.updatecell([3,3], player=player)
    #     captured = capsys.readouterr()
    #     assert 'Invalid move, please try again' in captured.out
    def testDispb(self):
        board = Board()
        player = Player("X")
        board.display()
