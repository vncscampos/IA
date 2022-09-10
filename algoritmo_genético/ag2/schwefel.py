from individuo import Individuo
import math

class Schwefel(Individuo):
    def __init__(self, chromosome):
        super().__init__(chromosome)
    
    def evaluate(self) -> float:
        sum1 = 0
        for i in range(len(self.chromosome)):
            sum1 += sum1 + self.chromosome[i] * math.sin(math.sqrt(abs(self.chromosome[i])))

        return 418.9829 * len(self.chromosome) - sum1
