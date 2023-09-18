from module.players.manager import PlayerManager
from module.game.manager import GameManager


player1_name = "Tony"
player2_name = "Arnaldo"

players = {"player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", ""]},
"player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}}

player1 = PlayerManager(player1_name, players["player1"])
player2 = PlayerManager(player2_name, players["player2"])

game = GameManager()

game.game_add_player(player1)
game.game_add_player(player2)

game.game_process()
stories = game.game_get_list_story()

for story in stories:
    print(story)