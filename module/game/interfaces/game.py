from module.players.interfaces.player import PlayerManagerInterface
from module.keys.interfaces.keys import KeyManagerInterface

class GameInitInterface:
    game_init_turn:int
    game_end_turn:int
    game_players:list
    game_init:bool
    game_end:bool
    game_turn:int
    game_max_turn:int
    game_turn_player_init:PlayerManagerInterface
    game_turn_player:PlayerManagerInterface
    game_no_turn_player:PlayerManagerInterface
    game_story:list
    game_combo:list
    game_data:list
    game_max_player:int
    
class GameActionsInterface(GameInitInterface):
    
    def game_execute_init(self) -> None:
        pass
    
    def game_execute_end(self) -> None:
        pass
    
    def game_execute_turn_init_player(self) -> None:
        pass

class GamePlayerInterface(GameInitInterface):
    
    def game_add_player(self, player:PlayerManagerInterface) -> None:
        pass
    
    def game_count_actions(self, player:PlayerManagerInterface) -> dict:
        pass


class GameStatusInterface(GameInitInterface):
    
    def game_get_turn_player(self) ->PlayerManagerInterface:
        pass

    def game_get_list_story(self) -> list:
        pass

class GameManagerInteface(GameActionsInterface, GamePlayerInterface, 
                          GameStatusInterface, KeyManagerInterface):
    
    
    def __init__(self) ->None:
        pass
    
    def game_verify_turn_player(self) -> None:
        pass
    
    def game_process_verify_turn_player(self, game_players:list) -> list:
        pass

    def game_process_max_turn(self) ->None:
        pass
    
    def game_order_turn(self) ->None:
        pass
    
    def game_all_data_combo(self) ->None:
        pass
    
    def game_create_relate(self) ->None:
        pass
    
    def game_relate_move(self, moves:list, name_player1:str) ->str:
        pass
    
    def game_relate_combo(self, combo:str, name_player2:str) ->str:
        pass
    
    def game_process(self) ->None:
        pass