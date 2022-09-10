from individuo import Individuo
from math import pow

class DifferentPower(Individuo):
    def __init__(self, chromosome):
        super().__init__(chromosome)
    
    def evaluate(self) -> float:
        dimension = len(self.chromosome)
        result = 0
        for i in range(dimension):
            xi = self.chromosome[i]
            result += pow(abs(xi), (i+1))
        return result
