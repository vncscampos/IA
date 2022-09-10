from individuo import Individuo
import math

class CrossInTray(Individuo):
    def __init__(self, chromosome):
        super().__init__(chromosome)
    
    def evaluate(self) -> float:
        x1 = self.chromosome[0]
        x2 = self.chromosome[1]

        fact1 = math.sin(x1) * math.sin(x2)
        fact2 = math.exp(abs(100 - math.sqrt(x1*x1 + x2*x2) / math.pi))

        y = -0.0001 * math.pow(abs(fact1 * fact2) + 1, 0.1)
        
        return y
