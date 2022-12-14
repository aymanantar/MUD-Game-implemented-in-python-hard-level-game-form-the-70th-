import unittest

from scripts.player import Player

class PositionChangingFunctions (unittest.TestCase) :
    ## 4 Dirctions 
    
    ## x axis
    def test_GoNorth(self):
        player = Player ("Ayman", "Male", "Tuleca", 50 , 50  )
        old_Xcoordinate = player.GetX()
        player.north()
        self.assertEqual(  player.GetX() , old_Xcoordinate +  1 )
        
    def test_GoSouth(self):
        player = Player ("Ayman", "Male", "Tuleca", 50 , 50 )
        old_Xcoordinate = player.GetX()
        player.south()
        self.assertEqual(  player.GetX() ,  old_Xcoordinate - 1 )
    ## y axis
    def test_GoEast(self):
        player = Player ("Ayman", "Male", "Tuleca", 50 , 50 )
        old_Ycoordinate = player.GetY()
        player.east()
        self.assertEqual(  player.GetY() , old_Ycoordinate + 1 )     
    def test_GoWest(self):
        player = Player ("Ayman", "Male", "Tuleca", 50 , 50 )
        old_Ycoordinate = player.GetY()
        player.west()
        self.assertEqual(  player.GetY(), old_Ycoordinate - 1 )             
        
        
   
        



if __name__ == '__main__':
    unittest.main()
