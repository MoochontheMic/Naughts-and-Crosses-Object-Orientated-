from Board import Board
from Player import Player


# CAPITALIZE constants here
gameover = False
draw = False
winner = ' '

winpos1 =[[0,0],[0,1],[0,2]]
winpos2 =[[1,0],[1,1],[1,2]]
winpos3 =[[2,0],[2,1],[2,2]]

winpos4 =[[0,0],[1,0],[2,0]]
winpos5 =[[0,1],[1,1],[2,1]]
winpos6 =[[0,2],[1,2],[2,2]]

winpos7 = [[0,0],[1,1],[2,2]]
winpos8 = [[0,2],[1,1],[2,0]]

allwinpos = [winpos1,winpos2,winpos3,winpos4,winpos5,winpos6,winpos7,winpos8]


class Rules():# class for the winning conditions

    def __init__(self):
        self.winner = None

    def wincheck(self, player: Player, board: Board):
        """checks player has won"""

        for winningMove in allwinpos:
            count = 0
            for coordinate in winningMove:
                x, y = coordinate[0], coordinate[1]
                # print('-------------------------')
                # print (board.cells)
                # print('-------------------------')
                if board.cells[x][y] == player.name:
                    count += 1
                    if count == 3:
                        self.gameover = True
                        self.winner = player.name
                        break
                    

    def drawcheck(self,turn):#checks for a draw
        if turn == 9:
            self.gameover = True
            self.draw = True
