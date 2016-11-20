import numpy as np
from copy import deepcopy


class Leaderboard:
    def __init__(self, data_file):
        self.results = 0

        with open(data_file) as file:
            first_line = True
            i = 0
            for line in file:
                if first_line:
                    first_line = False
                    self.results = [None] * int(line)
                    continue
                splited_line = line.split(" ")
                j = 0
                for value in splited_line:
                    splited_line[j] = int(value)
                    j += 1
                self.results[i] = splited_line
                i += 1
            self.results = np.matrix(self.results)

    def get_permutation(self, phenotype):
        new_result = deepcopy(self.results[phenotype])
        new_result[:, :] = new_result[:, phenotype]
        return new_result

    def evaluate_permutation(self, phenotype):
        permutation = self.get_permutation(phenotype)
        quality = np.sum(np.triu(permutation, 0))
        return quality

    def print(self, phenotype):
        to_print = self.get_permutation(phenotype)
        for line in to_print:
            print(line)

    def get_number_of_players(self):
        return len(self.results)
