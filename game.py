from ast import List
from Board import Board
from Player import Player
from Rules import Rules


class Game():
    """
    Main game class
    """
    def __init__(self):
        self.currentPlayerX = True
        

    def extractCoordinates(self, coordinate: str):
        try:
            # TODO: Update to account for not enough arguments
            formattedCoordinate = coordinate.replace(' ', '').split(',')
            x = int(formattedCoordinate[0])
            y = int(formattedCoordinate[1])
        except ValueError:
            print('Coordinates must be integers')
            self.extractCoordinates()

        return [x-1, y-1]

    def __main__(self):
        board = Board()
        player1 = Player("X")
        player2 = Player("O")
        rules = Rules()
        counter = 0
        draw = False

        while not rules.gameover:
            board.display()

            move = input("Choose coordinate of move with x,y\n")    
            move = self.extractCoordinates(move)

            currentPlayer = player1 if self.currentPlayerX else player2

            if board.updatecell(move, player=currentPlayer):
                self.currentPlayerX = not self.currentPlayerX
                rules.wincheck(currentPlayer, board)
                counter += 1
            # if not any([item for item in board.cells if item == ' ']):
            if counter == 9:
                print('COUNTER: ', counter)
                draw = True
                rules.gameover = True
        board.display()
        if not draw:
            if currentPlayer == player1:
                print('Winner is X!')
            else:
                print('Winner is O!')
        else:
            print('Game is a draw')
    # if __name__ == '__main__':
Game().__main__()
