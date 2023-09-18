class EnergyInitInterface:
    energy_initial:int
    energy_final:int
    energy_current:int
    
class EnergyStatusInterface(EnergyInitInterface):
    
    def get_initial_energy(self) -> int:
        pass
    
    def get_current_energy(self) -> int:
        pass
    
    def get_final_energy(self) -> int:
        pass

class EnergyManagerInterface(EnergyStatusInterface):
    def reduce_energy(self, value:int) -> None:
        pass