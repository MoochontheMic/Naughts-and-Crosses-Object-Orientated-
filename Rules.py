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