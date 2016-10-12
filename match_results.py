class MatchResults:
    def __init__(self):
        with open("data/ATP_3.dat") as file:
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

    def get_permutation(self, phenotype):
        j = 0
        results = self.results.copy()
        for line in results:
            results[j] = [line[i - 1] for i in phenotype]
            j += 1
        return [results[i - 1] for i in phenotype]

    def evaluate_permutation(self, phenotype):
        permutation = self.get_permutation(phenotype)
        quality = 0
        for i in range(0, len(permutation) - 1):
            for j in range(i + 1, len(permutation)):
                quality += permutation[i][j]
        return quality

    def print(self, phenotype):
        to_print = self.get_permutation(phenotype)
        for line in to_print:
            print(line)
