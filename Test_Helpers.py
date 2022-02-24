# import sys
# sys.path.append("..")
from Board import Board
from Player import Player
from Rules import Rules
import numpy as np
import os

Turn = 0
gameover = False
board = Board()
wincheck = Rules()
class test_helpers():
    
    def TSTINPUT(self,array):
        #wincheck.gameover == False
        wincheck.winner == " "
        Turn=0
        a = np.array(array)
        while wincheck.gameover == False: #loops the turns until theres a win or draw

            
            O_choice = a[Turn] #p1 turn
            board.updatecell(O_choice-1, Player)
            Turn += 1
        
            wincheck.Ocheck(board.cells)
            if wincheck.gameover == True:
                continue
        #these see if the game ended after p1s turn
            wincheck.drawcheck(Turn)
            if wincheck.gameover == True:
                continue
        
            
            X_choice = a[Turn]#p2 turn
            board.updatecell(X_choice - 1 , Pieces.player2)
            Turn += 1
        
            wincheck.xcheck(board.cells)
        #checks if the game ended after p2 turn
        
        
        if wincheck.winner == "O":
            return 1
        else:
            if wincheck.winner == "X":
                return 2
            else:
                return 3
        

#print(test_helpers().TSTINPUT([1,4,2,5,3,6,7,8,9]))