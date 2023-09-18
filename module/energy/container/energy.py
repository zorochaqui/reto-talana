from module.energy.interfaces.energy import EnergyInitInterface, EnergyStatusInterface

class EnergyStatus(EnergyStatusInterface, EnergyInitInterface):
    
    def get_initial_energy(self) -> int:
        return self.energy_initial
    
    def get_current_energy(self) -> int:
        return self.energy_current
    
    def get_final_energy(self) -> int:
        return self.energy_final