from typing import List
from nQueens import nQueens
import random


class AlgoritmoGenetico:
    def __init__(self):
        self.__population: List[nQueens] = []
        self.__is_minimization = True

    def execute(self, nGen: int, nInd: int, elitism: int, numQueens: int):
        # Iniciando população
        for i in range(nInd):
            gen = random.sample(list(range(numQueens)), k=numQueens)
            self.__population.append(nQueens(gen, numQueens))

        for gen in range(nGen):
            aux_population: List[nQueens] = []
            aux_population.extend(self.__population)
            aux_population.extend(self.__get_sons())
            aux_population.extend(self.__get_mutations())

            self.__population = aux_population
            elite = sorted(self.__population, key=lambda individual: individual.chromosome)[
                :elitism]

            self.__selection(nInd - elitism)
            self.__population.extend(elite)
            self.__printer(gen)

    def __get_sons(self):
        parents = self.__population.copy()
        sons = []

        for i in range(int(len(self.__population)/2)):
            p1 = parents.pop(random.randint(0, len(parents)-1))
            p2 = parents.pop(random.randint(0, len(parents)-1))
            son = p1.crossover(p2)
            sons.extend(son)

        return sons

    def __get_mutations(self):
        mutations = []
        for individual in self.__population:
            aux_mutation = individual.mutate()
            mutations.append(aux_mutation)
        return mutations

    def __evaluation(self):
        total = 0

        for individual in self.__population:
            if self.__is_minimization:
                total += 1/(individual.get_evaluate()+1)
            else:
                total += individual.get_evaluate()
        return total

    def __wheel(self, raffled):
        selected = None
        sum = 0

        for individual in self.__population:
            if self.__is_minimization:
                sum += 1/(individual.get_evaluate()+1)
            else:
                sum += individual.get_evaluate()

            if sum >= raffled:
                selected = individual
                break

        return selected

    def __selection(self, nInd: int):
        selected_genes = []
        total = self.__evaluation()

        for i in range(nInd):
            if self.__is_minimization:
                rand = random.uniform(0,total) 
            else:
                rand = random.randint(0,total)

            value = self.__wheel(rand)
            selected_genes.append(value)

        self.__population = selected_genes

    def __printer(self, gen: int):
        best = self.__population[0]

        for individual in self.__population:
            if self.__is_minimization and individual.get_evaluate() <= best.get_evaluate():
                best = individual
            elif not self.__is_minimization and individual.get_evaluate() >= best.get_evaluate():
                best = individual
        print('Geração: {} Individuo: {} Colisão: {}'.format(
            gen, best.chromosome, best.fitness))
