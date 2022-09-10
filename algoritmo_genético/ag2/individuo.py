from functools import reduce
import random
import math
from abc import ABC, abstractmethod 

class Individuo(ABC):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = 0.0
        self.evaluated = False

    #Arithmetic crossover
    def crossover(self, parent: list, alfa=0.33):
        son1 = []
        son2 = []
        for i in range(len(self.chromosome)):
            son1.append((1-alfa) * self.chromosome[i] + alfa * parent[i])
            son2.append((1-alfa) * parent[i] + alfa * self.chromosome[i])  

        return [son1,son2]

    #Gaussian mutation
    def mutate(self, mutation_rate=0.0):
        mutant = []

        for gene in self.chromosome:
            rand_rate = random.random()
            if rand_rate >= mutation_rate:
                alfa = random.gauss(mu=0, sigma=0.0000000000000001)   
                mutant.append(gene + alfa)
            else:
                mutant.append(gene)
        if mutant == self.chromosome:
            index = random.randint(0,len(self.chromosome)-1)
            alfa = random.gauss(mu=0, sigma=0.0000000000000001)
            mutant[index] += alfa
        
        return mutant
        
    @abstractmethod
    def evaluate(self):
        pass

    def get_evaluate(self):
        if not self.evaluated:
            self.evaluated = True
            self.fitness = self.evaluate()
        return self.fitness