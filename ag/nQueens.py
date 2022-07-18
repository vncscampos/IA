import random


class nQueens:

    def __init__(self, chromosome: list, nQueens):
        self.nQueens = nQueens
        self.chromosome = chromosome
        self.fitness = 0
        self.evaluated = False

    def crossover(self, individual):
        son1 = self.chromosome[:4]
        son2 = individual.chromosome[:4]

        self.crossover_second_part(individual.chromosome, son1)
        self.crossover_second_part(self.chromosome, son2)

        self.check(son1)
        self.check(son2)

        return [nQueens(son1, self.nQueens), nQueens(son2, self.nQueens)]

    def crossover_second_part(self, chromosome: list, son: list):
        for i in chromosome[4:]:
            try:
                check = son.index(i)
                son.append(-1)
            except ValueError:
                son.append(i)

    def mutate(self, rate=0.05):
        mutation = self.chromosome.copy()
        aux_mutation = False

        for mutation_index in range(self.nQueens):
            random_rate = random.random()
            if random_rate >= rate:

                new_chromosome = mutation[mutation_index]

                while new_chromosome == mutation[mutation_index]:
                    new_chromosome = random.randint(0, self.nQueens-1)

                index = mutation.index(new_chromosome)
                mutation[index] = mutation[mutation_index]
                mutation[mutation_index] = new_chromosome

                aux_mutation = True

        if not aux_mutation:
            rand_pos = random.randint(0, self.nQueens-1)
            mutation = self.swap(mutation, rand_pos)
        return nQueens(mutation, self.nQueens)

    def evaluate(self):
        eval = 0
        for i in range(self.nQueens):
            for j in range(i + 1, self.nQueens):
                value = abs(j - i)
                if(self.chromosome[i] == self.chromosome[j] or self.chromosome[i] == self.chromosome[j] - value or self.chromosome[i] == self.chromosome[j] + value):
                    eval += 1
        return eval

    def get_evaluate(self):
        if not self.evaluated:
            self.fitness = self.evaluate()
            self.evaluated = True
        return self.fitness

    def check(self, chromosome: list):
        check = []

        for i in range(len(chromosome)):
            try:
                chromosome.index(i)
            except ValueError:
                check.append(i)

        while len(check) != 0:
            rand = random.randint(0, len(check)-1)
            index = chromosome.index(-1)
            checked_value = check.pop(rand)
            chromosome.pop(index)

            chromosome.insert(index, checked_value)
