from module.players.container.player import PlayerVerify
from module.players.interfaces.player import PlayerManagerInterface
from module.energy.manager import EnergyManager
from constant.errors import ERROR_INT, ERROR_STRING, ERROR_DICT
from constant.statics import PLAYER_TURN_INIT

class PlayerManager(PlayerManagerInterface, PlayerVerify, EnergyManager):
    
    player_turn:int = PLAYER_TURN_INIT
    player_max_turn:int = 0
    
    def __init__(self, name:str, data:dict) -> None:
        if not isinstance(name, str):
            raise ValueError(ERROR_STRING)
            
        if not isinstance(data, dict):
            raise ValueError(ERROR_DICT)
        
        self.player_name = name
        self.player_data = data
        self.player_max_turn = len(data["movimientos"])
    
    def player_update_turn(self, turn:int) ->None:
        if isinstance(turn, int):
            self.player_turn = turn
        else:
            raise ValueError(ERROR_INT)
    
    def player_data_turn(self, turn:int) -> list:
        self._player_verify_data()
        self._player_verify_turn_data(turn)
        movements = self.player_data["movimientos"][turn]
        punches = self.player_data["golpes"][turn]
        return movements, punches
    
    