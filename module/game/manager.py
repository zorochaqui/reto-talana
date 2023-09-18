from module.game.interfaces.game import GameManagerInteface
from module.game.container.game import GameActions, GamePlayer, GameStatus
from module.players.interfaces.player import PlayerManagerInterface
from module.keys.manager import KeyManager
from constant.statics import MAX_PLAYER
from constant.errors import ERROR_MAX_ADD_PLAYER

class GameManager(GameManagerInteface, GameActions, GamePlayer, GameStatus, KeyManager):
    
    game_players:list = []
    game_story:list = []
    game_turn:int = 0
    game_max_player:int = MAX_PLAYER
    game_max_turn:int = 0
    game_combo:list = []
    game_data:list = []
    
    def __init__(self) ->None:
        self.key_init_keys_list()
        self.key_init_combo_list()
    
    def game_verify_turn_player(self) -> None:  

        player1, player2 = self.game_process_verify_turn_player(self.game_players)
        self.game_turn_player_init = player1
        self.game_turn_player = player1
        self.game_no_turn_player = player2
        
    def game_process_verify_turn_player(self, game_players:list) ->list:
        if len(game_players) < self.game_max_player:
            raise ValueError(ERROR_MAX_ADD_PLAYER)

        minor_player = game_players[0]
        minor_player_data = self.game_count_actions(minor_player)
        minor_player_combination = minor_player_data["combination"]
        minor_player_movement = minor_player_data["movement"]
        minor_player_punch = minor_player_data["punch"]

        second_minor_player = None
        second_minor_combination = float("inf")
        second_minor_movement = float("inf")
        second_minor_punch = float("inf")

        for player in game_players[1:]:
            other_player_data = self.game_count_actions(player)
            other_player_combination = other_player_data["combination"]
            other_player_movement = other_player_data["movement"]
            other_player_punch = other_player_data["punch"]

            if other_player_combination < minor_player_combination or \
                (other_player_combination == minor_player_combination and other_player_movement < minor_player_movement) or \
                (other_player_combination == minor_player_combination and other_player_movement == minor_player_movement and other_player_punch < minor_player_punch):
                second_minor_player = minor_player
                second_minor_combination = minor_player_combination
                second_minor_movement = minor_player_movement
                second_minor_punch = minor_player_punch

                minor_player = player
                minor_player_combination = other_player_combination
                minor_player_movement = other_player_movement
                minor_player_punch = other_player_punch
            elif other_player_combination < second_minor_combination or \
                (other_player_combination == second_minor_combination and other_player_movement < second_minor_movement) or \
                (other_player_combination == second_minor_combination and other_player_movement == second_minor_movement and other_player_punch < second_minor_punch):
                second_minor_player = player
                second_minor_combination = other_player_combination
                second_minor_movement = other_player_movement
                second_minor_punch = other_player_punch

        return minor_player, second_minor_player

    def game_process_max_turn(self) ->None:
        
        player1 = self.game_turn_player.player_max_turn
        player2 = self.game_no_turn_player.player_max_turn
        max_turn = player1
        if player1 < player2:
            max_turn = player2
        self.game_max_turn = max_turn

    def game_order_turn(self) ->None:
        player1 = self.game_turn_player
        player2 = self.game_no_turn_player
        
        for i in range(self.game_max_turn):
    
            if i < player1.player_max_turn:
                move, punch = player1.player_data_turn(i)
                self.game_data.append({
                    "move":move,
                    "punch": punch,
                    "player_turn": player1,
                    "player_no_turn": player2
                })
            
            if i < player2.player_max_turn:
                move, punch = player2.player_data_turn(i)
                self.game_data.append({
                    "move":move,
                    "punch": punch,
                    "player_turn": player2,
                    "player_no_turn": player1
                })
    
    def game_all_data_combo(self) ->None:
        combos = self.game_data
        for combo in combos:
            data = self.key_search_action(combo["move"], combo["punch"])
            self.game_combo.append({"data": data, 
                                    "player_turn": combo["player_turn"],
                                    "player_no_turn": combo["player_no_turn"]
                                    })
   
    def game_create_relate(self) ->None:
        
        winner = ""
        text_move = ""
        text_combo = ""
        for data in self.game_combo:
            
            if data["player_turn"].energy_current >= 1 and \
                data["player_no_turn"].energy_current >= 1:
                text_move = self.game_relate_move(data["data"]["move"], data["player_turn"].player_name)
                text_combo = self.game_relate_combo(data["data"]["name_combo"], data["player_no_turn"].player_name)
                self.game_story.append(text_move + text_combo)
                data["player_no_turn"].reduce_energy(data["data"]["energy"])
                
                if data["player_no_turn"].energy_current == 0:
                    self.game_story.append(f'{data["player_turn"].player_name} Gana la pelea y aun le queda {data["player_turn"].energy_current} de energía')
                    
    
    def game_relate_move(self, moves:list, name_player1:str) ->str:
        text_move = ""
        for move in moves:
            text_move = text_move + " " + move
        
        if text_move.strip() != "":
            text_move = name_player1 + " se mueve " + text_move
        else:
            text_move = name_player1
        
        return text_move
    
    def game_relate_combo(self, combo:str, name_player2:str) ->str:
        
        text_combo = ""
        if combo.strip() != "":
            text_combo = " y conecta un/una "+combo + " a "+name_player2
        
        return text_combo       
    
    def game_process(self):
        self.game_verify_turn_player()
        self.game_process_max_turn()
        self.game_order_turn()
        self.game_all_data_combo()
        self.game_create_relate()