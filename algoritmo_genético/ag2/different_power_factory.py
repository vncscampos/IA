from different_power import DifferentPower
    
class DifferentPowerFactory:
    @staticmethod
    def factory(chromosome: list) -> DifferentPower:
        return DifferentPower(chromosome)
