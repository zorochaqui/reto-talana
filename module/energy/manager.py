from module.energy.container.energy import EnergyStatus
from module.energy.interfaces.energy import EnergyManagerInterface
from constant.statics import ENERGY_VAL_INITIAL, ENERGY_VAL_FINAL
from constant.errors import ENERGIA_ERROR_END, ERROR_INT

class EnergyManager(EnergyManagerInterface, EnergyStatus):
    
    energy_initial:int = ENERGY_VAL_INITIAL
    energy_final:int = ENERGY_VAL_FINAL
    energy_current:int = ENERGY_VAL_INITIAL
    
    def reduce_energy(self, value:int) -> None:
        if not isinstance(value, int):
            raise ValueError(ERROR_INT)
        
        if self.energy_current == self.energy_final:
            raise ValueError(ENERGIA_ERROR_END)
        
        self.energy_current = max(self.energy_current - value, self.energy_final)