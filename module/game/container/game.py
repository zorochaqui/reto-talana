from module.players.interfaces.player import PlayerManagerInterface
from module.game.interfaces.game import GameInitInterface,GameActionsInterface, \
                                        GamePlayerInterface, GameStatusInterface
                                        
from constant.errors import ERROR_ADD_PLAYER

class GameActions(GameActionsInterface, GameInitInterface):
    
    def game_execute_init(self) -> None:
        self.game_init = True
    
    def game_execute_end(self) -> None:
        self.game_init = True
        self.game_end = True
    
    def game_execute_turn_init_player(self) -> None:
        pass

class GamePlayer(GamePlayerInterface, GameInitInterface):
    
    def game_add_player(self, player:PlayerManagerInterface) -> None:
        if isinstance(player, PlayerManagerInterface):
            if len(self.game_players) < self.game_max_player:
                self.game_players.append(player)
            else:
                raise ValueError(ERROR_ADD_PLAYER)
        else:
            raise ValueError(ERROR_ADD_PLAYER)
        
    def game_count_actions(self, player:PlayerManagerInterface) -> dict:
        
        movements = player.player_data["movimientos"]
        punches = player.player_data["golpes"]

        movement_count = len([movement for movement in movements if movement])
        punch_count = len([punch for punch in punches if punch])

        return {
            "combination": movement_count + punch_count,
            "movement": movement_count,
            "punch": punch_count,
        }
        
class GameStatus(GameStatusInterface, GameInitInterface):
    
    def game_get_turn_player(self) ->PlayerManagerInterface:
        return self.game_turn_player

    def game_get_list_story(self) -> list:
        return self.game_story