import unittest

from scripts.player import Player

class TestDecrementFunctions (unittest.TestCase) :
     ## decrement functions
    def test_SuhtGun_Dcrement(self):
        player = Player ("Ayman", "Male", "Tuleca", 99 , 99 ,0 ,100  )
        old_shutguns = player.GetShutGuns()
        player.ShutgunDecrement()
        self.assertEqual(  player.GetShutGuns() ,  old_shutguns - 1 )
    def test_Arrows_Dcrement(self):
        player = Player ("Ayman", "Male", "Tuleca", 99 , 99 ,0 ,100)
        old_arrows = player.GetArrows()
        player.ArrowsDecrement()
        self.assertEqual(  player.GetArrows() ,  old_arrows - 1 )
        
    def test_Health_Decrement(self):
        player = Player ("Ayman", "Male", "Tuleca", 99 , 99 , 0 ,100)
        old_health = player.GetHealth()
        player.HealthDecrement()
        self.assertEqual(  player.GetHealth() ,  old_health - 50 )     
        



if __name__ == '__main__':
    unittest.main()
