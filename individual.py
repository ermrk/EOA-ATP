import random
from copy import copy

import collections


class Individual:
    def __init__(self, leaderboard):
        self.phenotype = None
        self.quality = 0
        self.leaderboard = leaderboard

    def set_phenotype(self, phenotype):
        self.phenotype = phenotype
        self._evaluate()

    def _evaluate(self):
        self.quality = self.leaderboard.evaluate_permutation(self.phenotype)

    def generate(self, length):
        permutation = [None] * length
        for i in range(0, len(permutation)):
            permutation[i] = i + 1
        random.shuffle(permutation)
        self.set_phenotype(permutation)

    def mutate(self, n_mutations):
        for i in range(0,n_mutations):
            elementOne = random.randrange(0, len(self.phenotype))
            elementTwo=elementOne
            while (elementTwo == elementOne):
                elementTwo = random.randrange(0, len(self.phenotype))
            temp=self.phenotype[elementOne]
            self.phenotype[elementOne]=self.phenotype[elementTwo]
            self.phenotype[elementTwo]=temp
            self._evaluate()

    def cross(self,individual,n_cross):
        block_size=random.randrange(1,n_cross)
        my_phenotype= copy(self.phenotype)
        block_start = random.randrange(0, len(my_phenotype)-block_size)
        numbers=[]
        for i in range(block_start,block_start+block_size):
            numbers.append(my_phenotype[i])
        for i in range(block_start,block_start+block_size):
            for j in range(0,len(individual.phenotype)):
                if individual.phenotype[j] in numbers:
                    my_phenotype[i]=individual.phenotype[j]
        newIndividual = Individual(self.leaderboard)
        newIndividual.set_phenotype(my_phenotype)
        print([item for item, count in collections.Counter(my_phenotype).items() if count > 1])
        return newIndividual


    def __str__(self):
        return str(str(self.quality)+" "+str(self.phenotype))
