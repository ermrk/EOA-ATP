import random

import sys

from individual import Individual
from leaderboard import Leaderboard


def generate_initial_population(length, leaderboard):
    individual = Individual(leaderboard)
    individual.generate(length)
    return individual


def alter_individual(individual, position, difference):
    phenotype = individual.phenotype.copy()
    player = phenotype[position]
    phenotype[position] = phenotype[position - difference]
    phenotype[position - difference] = player
    altered_individual = Individual(leaderboard)
    altered_individual.set_phenotype(phenotype)
    return altered_individual


def is_valid_alterance(length, position, difference):
    if position - difference < 0:
        return False
    if position - difference > length - 1:
        return False
    return True


# load data
number_of_iterartions = int(sys.argv[2])
leaderboard = Leaderboard(sys.argv[1])
number_of_players = leaderboard.get_number_of_players()

# make initial individual
individual = generate_initial_population(number_of_players, leaderboard)

# calculate its quality
best_so_far = individual
print("G: " + str(best_so_far.quality) + ", " + str(best_so_far.phenotype))

# LOOP
difference = -1
position = 0

for i in range(0, number_of_iterartions):
    # try to improve it
    altered_individual = alter_individual(best_so_far, position, difference)
    # decide if we will accept it
    if altered_individual.quality > best_so_far.quality:
        best_so_far = altered_individual
        print(str(i) + ": " + str(best_so_far.quality) + ", " + str(best_so_far.phenotype))
        position = -1
    position += 1
    if position >= number_of_players + difference:
        position = 0
        difference -= 1
    if -difference >= leaderboard.get_number_of_players():
        position = 0
        difference = -1