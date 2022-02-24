import os
import unittest
from Board import Board
from Player import Player
from Rules import GameClass
from Test_Helpers import test_helpers
# import numpy as np




class TestGame(unittest.TestCase):
    def test_OX(self):
        self.assertEqual(test_helpers().TSTINPUT([1,4,2,5,3,6,7,8,9]),1)#owin
        self.assertEqual(test_helpers().TSTINPUT([5,3,8,2,1,9,6,4,7]),3)#draw
        #self.assertEqual(test_helpers().TSTINPUT([9,4,2,5,3,6,7,8,1]),2)#xwin

A=TestGame()
A.test_OX()