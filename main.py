import random

import sys
from copy import deepcopy

from individual import Individual
from leaderboard import Leaderboard
from logger import logger

# DONT FORGET TO ADD ONE TO ALL INDEXES OF PERMUTATION

generation_size = 20  # size of generation
tournament_size = 3  # how many random individuals compete for usage in the new generation
n_mutations = 2  # how many genes can we mutate at most
cross_rate = int(generation_size / 5)  # how many individuals do we cross
cross_size = 4  # how long block can we cross at most
local_search_length = 10  # how many improvements do I try for each individual
local_search_interval = 10  # start local search every n generations
break_loop = False


def generate_initial_population(length, leaderboard):
    generation = []
    for i in range(0, generation_size):
        individual = Individual(leaderboard)
        individual.generate(length)
        generation.append(individual)
    return generation
for problem_name in ["data/ATP_24.dat","data/ATP_50.dat","data/ATP_55.dat","data/ATP_111.dat","data/ATP_452.dat"]:
    for run in range(20):
        # load data
        number_of_iterartions = int(sys.argv[2])
        logger_var = logger("GALS/", problem_name.replace("data/","").replace(".dat","")+"_"+str(run) + ".txt")
        leaderboard = Leaderboard(problem_name, logger_var)
        number_of_players = leaderboard.get_number_of_players()

        # make initial population
        initial_generation = generate_initial_population(number_of_players, leaderboard)
        generation = initial_generation
        break_loop = False
        for k in range(0, number_of_iterartions):
            if logger_var.break_it():
                print("Break")
                break
            # evaluation of individuals
            best_individual = max(generation, key=lambda x: x.quality)
            print(str(k) + ": " + str(best_individual.quality))

            # local search
            if k % local_search_interval == 0 and k > 0:
                print("Local search")
                for i in range(0, len(generation)):
                    for j in range(0, local_search_length):

                        newIndividual = generation[i].improve()
                        if newIndividual.quality >= generation[i].quality:
                            generation[i] = newIndividual

                best_individual = max(generation, key=lambda x: x.quality)
                print(str(k) + " Local search: " + str(best_individual.quality))

            # keeping old individuals
            keeped_old_ones = best_individual

            # selection
            selected = []
            for i in range(0, generation_size - 1):
                selected_indexes = []
                for j in range(0, tournament_size):
                    index = random.randrange(0, len(generation))
                    while index in selected_indexes:
                        index = random.randrange(0, len(generation))
                    selected_indexes.append(index)
                selected_individuals = []
                for j in range(0, len(selected_indexes)):
                    selected_individuals.append(deepcopy(generation[selected_indexes[j]]))
                selected_individuals.sort(key=lambda x: x.quality, reverse=True)
                index = 0
                appended = False
                for _ in range(0, tournament_size - 1):
                    if random.randrange(0, 2) == 0:
                        appended = True
                        selected.append(deepcopy(selected_individuals[index]))
                        break
                    else:
                        index += 1
                if not appended:
                    selected.append(deepcopy(selected_individuals[len(selected_individuals) - 1]))

            # cross
            selected_indexes_cross = []
            selected_individuals_cross = []
            crossed_individuals = []
            if cross_rate != 0:
                for i in range(0, cross_rate):
                    index = random.randrange(0, len(selected))
                    while index in selected_indexes_cross:
                        index = random.randrange(0, len(selected))
                    selected_indexes_cross.append(index)
                for j in range(0, len(selected_indexes_cross)):
                    selected_individuals_cross.append(selected[selected_indexes_cross[j]])
                for i in range(0, int(cross_rate / 2)):
                    indexOne = random.randrange(0, len(selected_individuals_cross))
                    indexTwo = random.randrange(0, len(selected_individuals_cross))
                    while indexTwo == indexOne:
                        indexTwo = random.randrange(0, len(selected_individuals_cross))
                    crossed_individuals.append(
                        selected_individuals_cross[indexOne].cross(selected_individuals_cross[indexTwo], cross_size))
                    crossed_individuals.append(
                        selected_individuals_cross[indexTwo].cross(selected_individuals_cross[indexOne], cross_size))

            # mutation
            # mutate not crossed
            mutated_individuals = []
            for i in range(0, len(selected)):
                if i not in selected_indexes_cross:
                    s = deepcopy(selected[i])
                    s.mutate(n_mutations)
                    mutated_individuals.append(s)
            # mutate crossed
            for i in range(0, len(crossed_individuals)):
                s = crossed_individuals[i]
                s.mutate(n_mutations)

            generation = [deepcopy(keeped_old_ones)] + deepcopy(crossed_individuals) + deepcopy(mutated_individuals)