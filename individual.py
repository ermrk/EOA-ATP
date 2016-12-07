import random
from copy import deepcopy


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
            permutation[i] = i
        random.shuffle(permutation)
        self.set_phenotype(permutation)

    def mutate(self, n_mutations):
        for i in range(1, n_mutations):
            elementOne = random.randrange(0, len(self.phenotype))
            elementTwo = elementOne
            while (elementTwo == elementOne):
                elementTwo = random.randrange(0, len(self.phenotype))
            temp = self.phenotype[elementOne]
            self.phenotype[elementOne] = self.phenotype[elementTwo]
            self.phenotype[elementTwo] = temp
        self._evaluate()

    def cross(self, individual, n_cross):
        my_phenotype = deepcopy(self.phenotype)
        numbers = []
        indexes_of_numbers = []
        actual_crosses = random.randrange(1, n_cross)
        for i in range(0, actual_crosses):
            index = random.randrange(0, len(my_phenotype))
            while index in indexes_of_numbers:
                index = random.randrange(0, len(my_phenotype))
            indexes_of_numbers.append(index)
            numbers.append(my_phenotype[index])

        start = 0
        for i in range(0, len(indexes_of_numbers)):
            for j in range(start, len(individual.phenotype)):
                if individual.phenotype[j] in numbers:
                    my_phenotype[indexes_of_numbers[i]] = individual.phenotype[j]
                    start = j + 1
                    break
        newIndividual = Individual(self.leaderboard)
        newIndividual.set_phenotype(my_phenotype)
        # print([item for item, count in collections.Counter(my_phenotype).items() if count > 1])
        return newIndividual

    def improve(self):
        my_phenotype = deepcopy(self.phenotype)
        indexOne = random.randrange(0, len(my_phenotype))
        indexTwo = random.randrange(0, len(my_phenotype))
        while indexTwo == indexOne:
            indexTwo = random.randrange(0, len(my_phenotype))
        temp = my_phenotype[indexOne]
        my_phenotype[indexOne] = my_phenotype[indexTwo]
        my_phenotype[indexTwo] = temp
        newIndividual = Individual(self.leaderboard)
        newIndividual.set_phenotype(my_phenotype)
        return newIndividual

    def __str__(self):
        return str(str(self.quality) + " " + str(self.phenotype))
