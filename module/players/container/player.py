from module.players.interfaces.player import PlayerVerifyInterface, PlayerDataInterface, PlayerTurnInterface
from constant.errors import ERROR_MOVIMIENTOS_GOLPES, ERROR_POSICION_TURNO

class PlayerVerify(PlayerVerifyInterface,PlayerDataInterface, PlayerTurnInterface):
    
    def _player_verify_data(self) -> None:
        if "movimientos" not in self.player_data or "golpes" not in self.player_data:
            raise ValueError(ERROR_MOVIMIENTOS_GOLPES)
    
    def _player_verify_turn_data(self, turn:int) -> None:
        if turn < 0 or turn >= len(self.player_data["movimientos"]):
            raise ValueError(ERROR_POSICION_TURNO)
        