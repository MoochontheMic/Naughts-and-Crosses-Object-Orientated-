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
