from module.energy.interfaces.energy import EnergyManagerInterface

class PlayerInitInterface:
    player_name:str

class PlayerDataInterface:
    player_data:dict

class PlayerTurnInterface:
    player_turn:int
    player_max_turn:int

class PlayerVerifyInterface(PlayerDataInterface, PlayerTurnInterface, PlayerInitInterface):
    def _player_verify_data(self) -> None:
        pass
    
    def _player_verify_turn_data(self) -> None:
        pass

class PlayerManagerInterface(PlayerVerifyInterface, EnergyManagerInterface):
    
    def __init__(self) -> None:
        pass
    
    def player_update_turn(self, turn:int) -> None:
        pass
    
    def player_data_turn(self) -> list:
        pass