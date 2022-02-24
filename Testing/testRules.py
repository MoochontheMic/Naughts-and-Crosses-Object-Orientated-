from ..Board import Board
from ..Player import Player
from ..Rules import Rules


class TestRules():

    def testWinningMove(self):
        board = Board()
        player = Player('X')
        rules = Rules()
        board.cells = [["X","X"," "],[" "," "," "],[" "," "," "]]
        board.updatecell([2,0], player=player)
        rules.wincheck(player, board)
        assert rules.winner == 'X'


    def testDrawingMove(self):
        pass

    def testRegularMove(self):
        pass
