import random
from typing import List

from individuo import Individuo
class Ag:
    def __init__(self):
        self.population: List[Individuo] = []
        self.maximization = False
        self.factory = None
        self.best: List[Individuo] = []
        
    def initial_population(self, nInd: int, a:int, b:int, dimension: int):
        aux = []
        for i in range(nInd):
            individuo = []
            for j in range(dimension):
                gen = random.uniform(a, b)
                individuo.append(gen)
            aux.append(self.factory(individuo))

        self.population = aux

    def execute(self,nGen:int,nInd:int,elitism:int,maximization:bool,interval: tuple, dimension:int ,factory) -> None:
        self.factory = factory
        self.initial_population(nInd, interval[0], interval[1], dimension)
        
        self.maximization = maximization
        
        for gen in range(nGen):
            aux_population = []
            
            aux_population.extend(self.population)
            aux_population.extend(self.get_recombinations())
            aux_population.extend(self.get_mutations())

            self.population = self.selection(aux_population, nInd, elitism)

            bestInd = self.population[0]

            for i in range(len(self.population)):
                if(self.population[i].get_evaluate() < bestInd.get_evaluate()):
                    bestInd = self.population[i]

            self.best.append(bestInd)
        
        self.printer()
     
    def get_recombinations(self) -> list:
        offsprings = []
        parents = self.population.copy()

        for i in range(0,int(len(self.population)/2)):
            r1 = random.randint(0, len(parents)-1)
            p1 = parents[r1]
            parents.remove(p1)

            r2 = random.randint(0, len(parents)-1)
            p2 = parents[r2]
            parents.remove(p2)

            sons = p1.crossover(p2.chromosome)
            aux = [self.factory(i) for i in sons]
            offsprings.extend(aux)
        return offsprings

    def get_mutations(self) -> list:
        mutants = []
        parents = self.population.copy()

        for i in range(0, len(self.population)):
            r1 = random.randint(0, len(parents)-1)
            p1 = parents[r1]
            parents.remove(p1)

            mutated = p1.mutate()
            mutants.append(self.factory(mutated))

        return mutants
        
    def selection(self, aux_pop: List[Individuo], nInd: int, elitism:int):
        aux_pop = sorted(aux_pop, key=lambda individual: individual.chromosome)

        new_pop = []

        x = 0
        while(x < elitism):
            ind = aux_pop[0]
            aux_pop.remove(ind)
            new_pop.append(ind)
            x += 1
        
        rest = 0
        total = self.evaluation_total()
        while (rest < (nInd - elitism)):
            rand = random.uniform(0, total)

            roullete_sum = 0
            for gen in aux_pop:
                roullete_sum += 1 / (gen.get_evaluate() + 1)
                if(roullete_sum >= rand):
                    aux_pop.remove(gen)
                    new_pop.append(gen)
                    break

            rest += 1

        return new_pop
    
    def evaluation_total(self):
        total = 0

        for chromosome in self.population:
            if self.maximization: 
                total += chromosome.get_evaluate()
            else:
                total += 1/(chromosome.get_evaluate()+1)
        return total

    def printer(self):
        self.best = sorted(self.best, key=lambda individual: individual.fitness, reverse=True)
        for i in range(len(self.best)):
            print('Geração: {}\tIndivíduo: {}\tAvaliação: {}'.format(i, self.best[i].chromosome, self.best[i].fitness))

