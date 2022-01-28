import os
import unittest
os.system('cls')


class Board():
    def __init__(self):#initialises a matrix  that stores the moves
        self.cells = [" "," "," "," "," "," "," "," "," "]

    def display(self): #this makes a physical representation of the board
        print(" ",self.cells[0]," | ",self.cells[1]," | ",self.cells[2]," ")
        print("_________________")
        print(" ",self.cells[3]," | ",self.cells[4]," | ",self.cells[5]," ")
        print("_________________")
        print(" ",self.cells[6]," | ",self.cells[7]," | ",self.cells[8]," ")
        
    def updatecell(self, cellno, Player): #updates the representative matrix when the player moves
        if self.cells[cellno] == " ":
            self.cells[cellno] = Player

class Pieces(): #the players pieces
    player1 = "O"
    player2 = "X"
       
class GameClass():# class for the winning conditions
    gameover = False
    draw = False
    winpos1 =[0,3,6,0,1,2,0,2]
    winpos2 =[1,4,7,3,4,5,4,4]
    winpos3 =[2,5,8,6,7,8,8,6]
    
    def xcheck(self,array):# checks if p1 has won
        for i in range(0,8):
            if array[self.winpos1[i]] == "X" and array[self.winpos2[i]] == "X" and array[self.winpos3[i]] == "X":
                self.gameover = True
                self.winner = "X"
                continue
    def Ocheck(self,array):#checks if p2 has won
        for i in range(0,8):
            if array[self.winpos1[i]] == "O" and array[self.winpos2[i]] == "O" and array[self.winpos3[i]] == "O":
                self.gameover = True
                self.winner = "O"
                continue
    def drawcheck(self,turn):#checks for a draw
        if turn == 9:
            self.gameover = True
            self.draw = True
        


Turn = 0
gameover = False
board = Board()
wincheck = GameClass()

print("Naughts and Crosses for Two-Players")






while wincheck.gameover == False: #loops the turns until theres a win or draw

    os.system('cls')
    
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


def TSTINPUT (array):
    Turn = 0
    gameover = False
    board = Board()
    wincheck = GameClass()
    while wincheck.gameover == False: #loops the turns until theres a win or draw

        os.system('cls')
    
        board.display()
        O_choice = self.array[Turn] #p1 turn
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
        X_choice = self.array[Turn]#p2 turn
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
         



class TestGame(unittest.TestCase):
    def test_OX(self):
        self.assert(TSTINPUT([1,4,2,5,3,6,7,8,9]),3)
        self.assert(TSTINPUT([9,4,2,5,3,6,7,8,1]),2)
