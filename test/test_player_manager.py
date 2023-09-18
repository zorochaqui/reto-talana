import unittest
from module.players.manager import PlayerManager

class TestPlayerManager(unittest.TestCase):
    def setUp(self):
        name = "Tony"
        data = {"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2":
                {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}
        self.player_manager = PlayerManager(name, data["player1"])
    
    def tearDown(self):
        pass
    
    def test_player_update_turn(self):
        self.player_manager.player_update_turn(2)
        self.assertIsInstance(self.player_manager.player_turn, int)

    def test_player_data_turn(self):
        player_data = self.player_manager.player_data_turn()
        self.assertIsInstance(player_data, list)
        #self.assertEqual(len(player_data), 2) 

if __name__ == "__main__":
    unittest.main()