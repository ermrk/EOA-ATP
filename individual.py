import random


class Individual:
    def __init__(self, leaderboard):
        self.phenotype = None
        self.genotype = None
        self.quality = 0
        self.leaderboard = leaderboard

    def set_phenotype(self, phenotype):
        self.phenotype = phenotype
        self.genotype = self._encode(phenotype)
        self._evaluate()

    def set_genotype(self, genotype):
        self.genotype = genotype
        self.phenotype = self._decode(genotype)
        self._evaluate()

    def _encode(self, phenotype):
        genotype = [None] * len(phenotype)
        for i in range(0, len(phenotype)):
            genotype[i] = 0
            m = 0
            while phenotype[m] != i + 1:
                if phenotype[m] > i + 1:
                    genotype[i] += 1
                m += 1
        return genotype

    def _decode(self, inv):
        n = len(inv)
        n_inv = [None] + inv
        perm = [None] * (n + 1)
        pos = [0] * (n + 1)
        for i in range(n, 0, -1):
            for m in range(i + 1, n + 1):
                print(m)
                if pos[m] >= n_inv[i] + 1:
                    pos[m] += 1
            pos[i] = n_inv[i] + 1
        for i in range(1, n + 1):
            perm[pos[i]] = i
        return perm[1:n + 1]

    def _evaluate(self):
        self.quality = self.leaderboard.evaluate_permutation(self.phenotype)

    def generate(self, length):
        permutation = [None] * length
        for i in range(0, len(permutation)):
            permutation[i] = i + 1
        random.shuffle(permutation)
        self.set_phenotype(permutation)

    def __str__(self):
        return str(self.phenotype)
