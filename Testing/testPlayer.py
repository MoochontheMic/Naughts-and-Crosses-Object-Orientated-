from ..Player import Player

class TestPlayer():
    
    def testPlayerNameX(self):
        player = Player('X')

        assert player.name == 'X'
    
    
    def testPlayerNameO(self):
        player = Player('O')

        assert player.name == 'O'
