from abc import ABC, abstractmethod

class Individuo(ABC):
    
    def __init__(self):
        self._avaliated = False
        self._eval = 0
        super().__init__()

    @abstractmethod
    def crossover(self, individual):
        pass
    
    @abstractmethod
    def mutate(self):
        pass
    
    @abstractmethod
    def evaluate(self):
        pass

    def get_evaluate(self):
        if not self._avaliated:
            self._eval = self.evaluate()
            self._avaliated = True
        return  self._eval
