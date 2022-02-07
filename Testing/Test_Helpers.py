import sys
sys.path.append("C:\Users\lachl\source\repos\OOP")
from Board import Board
from Pieces import Pieces
from Rules import GameClass

Turn = 0
gameover = False
board = Board()
wincheck = GameClass()

def TSTINPUT (array):
    while wincheck.gameover == False: #loops the turns until theres a win or draw

        os.system('cls')
    
        board.display()
        O_choice = array[Turn] #p1 turn
        board.updatecell(O_choice-1, Pieces.player1)
        Turn += 1
    
        wincheck.Ocheck(board.cells)
        if wincheck.gameover == True:
            continue
    #these see if the game ended after p1s turn
        wincheck.drawcheck(Turn)
        if wincheck.gameover == True:
            continue
    
        board.display()
        X_choice = array[Turn]#p2 turn
        board.updatecell(X_choice - 1 , Pieces.player2)
        Turn += 1
    
        wincheck.xcheck(board.cells)
    #checks if the game ended after p2 turn
    
    board.display()
    if wincheck.draw == True:
       return 1
    else:
        if wincheck.winner == "X":
            return 2
        else:
            return 3