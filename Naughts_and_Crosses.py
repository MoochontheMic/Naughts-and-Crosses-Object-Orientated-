import os
from Board import Board
from Rules import Rules
os.system('cls')

print("Naughts and Crosses for Two-Players")
Turn = 0
gameover = False
board = Board()
wincheck = Rules()

while not wincheck.gameover: # Whilst the game isn't over

    #os.system('cls')
    
    board.display()
    O_choice = int(input("\nO) Choose a number between 1-9 inclusive to select a square: " )) #p1 turn
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
    X_choice = int(input("\nX) Choose a number between 1-9 inclusive to select a square: " ))#p2 turn
    board.updatecell(X_choice - 1 , Pieces.player2)
    Turn += 1
    
    wincheck.xcheck(board.cells)
    #checks if the game ended after p2 turn
    
board.display()
if wincheck.draw == True:
    print("Game was a draw")
else:
    print("Game winner is ", wincheck.winner)   
#prints the result
