import unittest

from scripts.player import Player

class TestIncrementFunctions (unittest.TestCase) :
    ## increment functions 
    def test_SuhtGun_Increment(self):
        player = Player ("Ayman", "Male", "Tuleca", 99 , 99 ,0 ,0 )
        old_shutguns = player.GetShutGuns()
        player.ShutGunIncrement()
        self.assertEqual(  player.GetShutGuns(),  old_shutguns+1 )
        
    def test_Arrows_Increment(self):
        player = Player ("Ayman", "Male", "Tuleca", 99 , 99 ,0 ,0 )
        old_arrows = player.GetArrows()
        player.ArrowsIncrement()
        self.assertEqual(  player.GetArrows() ,  old_arrows + 1 )
        
    def test_Health_Increment(self):
        player = Player ("Ayman", "Male", "Tuleca", 99 , 99 ,0 , 50)
        old_health = player.GetHealth()
        player.HealthIncrement()
        self.assertEqual(  player.GetHealth(), old_health + 50 )     
        
        
        
   
        



if __name__ == '__main__':
    unittest.main()
