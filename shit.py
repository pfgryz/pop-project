import numpy as np
from math import radians, cos, sin, asin, sqrt
import csv
from copy import deepcopy
from random import shuffle, randint, choice

NORTH_POLE = {}
NORTH_POLE['Latitude'] = 90
NORTH_POLE['Longitude'] = 0


def refactored(*args, **kwargs):
    pass


def get_data_from_csv_file(path):
    with open(path, "r") as file_handle:
        reader = csv.DictReader(file_handle)
        list_of_data = []
        for dictionary in reader:
            # żeby id odpowiadało pozycji w liście
            dictionary['NewId'] = len(list_of_data)
            list_of_data.append(dictionary)
        return list_of_data

def evolutionary_algorithm(generate_population, rating_function, evaluation,
                           selection, mutation,
                           selection_parameters_tournament_size,
                           selection_parameters_tournament_function,
                           selection_parameters_probability,
                           mutation_parameters_probability,
                           population_size, number_of_populations, iterations):
    populations = generate_population(population_size, number_of_populations)
    t = 1

    ratings = rating_function(populations, evaluation)
    best_rating = min(ratings)
    best_individual = populations[np.argmin(ratings)]
    best_individuals = []
    best_individuals.append(best_individual)

    while t < iterations:
        succesion = []

        for population in populations:
            succesion_i = mutation(population, mutation_parameters_probability)
            succesion.append(succesion_i)
        populations = deepcopy(
            selection(succesion, selection_parameters_tournament_size,
                      selection_parameters_tournament_function, evaluation,
                      selection_parameters_probability))

        ratings = rating_function(populations, evaluation)
        best_rating_t = min(ratings)
        best_individual_t = populations[np.argmin(ratings)]
        best_individuals.append(best_individual_t)

        if best_rating >= best_rating_t:
            best_rating = best_rating_t
            best_individual = best_individual_t
        print(t)
        t += 1

    return best_individuals, (best_individual, best_rating)

# DATA = get_data_from_csv_file('POP/gifts1000.csv')[0:50]
#
# best_individuals, betsest = evolutionary_algorithm(population_uniform,
#                                                    rating_function, wrw,
#                                                    tournament_selection,
#                                                    mutation_swap_and_run,
#                                                    2, tournament_2, 0.75,
#                                                    0.5,
#                                                    20, 100, 1000)
#
# print(best_individuals)
# print(betsest)
