from ..Board import Board
from ..Player import Player
from ..Rules import Rules


class TestRules():

    def testWinningMove(self):
        board = Board()
        player = Player('X')
        rules = Rules()
        board.cells = [["X"," "," "],["X"," "," "],[" "," "," "]]
        board.display()
        board.updatecell([2,0], player=player)
        board.display()
        rules.wincheck(player, board)
        assert rules.winner == 'X'


    def testDrawingMove(self):
        pass

    def testRegularMove(self):
        pass
