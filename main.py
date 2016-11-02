import random

import sys
from copy import copy

from individual import Individual
from leaderboard import Leaderboard

generation_size = 100
tournament_size = 3
keep_old_ones = 10
n_mutations = 3
cross_rate = 20
cross_size = 5


def generate_initial_population(length, leaderboard):
    generation = []
    for i in range(0, generation_size):
        individual = Individual(leaderboard)
        individual.generate(length)
        generation.append(individual)
    return generation


# load data
number_of_iterartions = int(sys.argv[2])
leaderboard = Leaderboard(sys.argv[1])
number_of_players = leaderboard.get_number_of_players()

# make initial population
initial_generation = generate_initial_population(number_of_players, leaderboard)
generation = initial_generation
for k in range(0, number_of_iterartions):
    generation.sort(key=lambda x: x.quality, reverse=True)
    print(str(k) + ": " + str(generation[0].quality))
    # keeping old individuals
    selected = generation[0:keep_old_ones]
    # selection
    for i in range(0, generation_size - keep_old_ones):
        selected_indexes = []
        for j in range(0, tournament_size):
            index = random.randrange(0, len(generation))
            while index in selected_indexes:
                index = random.randrange(0, len(generation))
            selected_indexes.append(index)
        selected_individuals = []
        for j in range(0, len(selected_indexes)):
            selected_individuals.append(generation[selected_indexes[j]])
        selected_individuals.sort(key=lambda x: x.quality, reverse=True)
        selected.append(copy(selected_individuals[0]))

    #cross
    selected_indexes_cross = []
    selected_individuals_cross = []
    crossed_individuals = []
    mutated_individuals=[]
    for i in range(0, cross_rate):
        index = random.randrange(0, len(generation))
        while index in selected_indexes_cross:
            index = random.randrange(0, len(generation))
        selected_indexes_cross.append(index)
    for j in range(0, len(selected_indexes_cross)):
        selected_individuals_cross.append(generation[selected_indexes_cross[j]])
    for i in range(0, 10):
        indexOne = random.randrange(0, len(selected_individuals_cross))
        indexTwo = random.randrange(0, len(selected_individuals_cross))
        while indexTwo == indexOne:
            indexTwo = random.randrange(0, len(selected_individuals_cross))
        crossed_individuals.append(selected_individuals_cross[indexOne].cross(selected_individuals_cross[indexTwo], 5))
        crossed_individuals.append(selected_individuals_cross[indexTwo].cross(selected_individuals_cross[indexOne], 5))

    # mutation
    for i in range(0, len(selected)):
        if i not in selected_indexes_cross:
            s=copy(selected[i])
            s.mutate(n_mutations)
            mutated_individuals.append(s)

    generation = copy(crossed_individuals)+copy(mutated_individuals)
