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


def rating_function(population, rating_criterion_function):
    return [rating_criterion_function(individual) for individual in population]


def mutation_random_gift_into_random_position(population, probability):
    # można, bo kolejność sań nie ma znaczenia
    shuffle(population)
    i = 0
    while i < len(population):
        if np.random.uniform() < probability:
            if len(population[i]) == 0:
                break
            chosen_gift = choice(population[i])
            population[i].remove(chosen_gift)
            population[i] = fix_present_position(population[i])
            if len(population[i + 1]) == 0:
                population[i + 1].append(chosen_gift)
            else:
                place = len(population[i + 1]) - 1
                population[i + 1].insert(place, chosen_gift)
            population[i + 1] = fix_present_position(population[i + 1])
        i += 2
    return population


# pewnie niepotrzebne bo źle zrozumiałam wariant drugi, ale jeśli się przyda to nazwa do zmiany
def mutation_swap_and_run(population, probability):
    new_population = mutation_move_last_gift(population, probability)
    p = mutation_swap_random_gifts_in_sleigh(new_population, probability)
    return p


def mutation_move_last_gift(population, probability):
    shuffle(population)
    i = 0
    while i < len(population):
        if np.random.uniform() < probability:
            if len(population[i]) == 0:
                break
            population[i + 1].append(population[i][-1])
            population[i].remove(population[i][-1])
            population[i + 1] = fix_present_position(population[i + 1])
        i += 2
    return population


def mutation_swap_random_gifts_in_sleigh(population, probability):
    for sleigh in population:
        if np.random.uniform() < probability:
            if len(sleigh) == 0 or len(sleigh) == 1:
                break
            first = randint(0, len(sleigh) - 1)
            second = first
            while first == second:
                second = randint(0, len(sleigh) - 1)
            sleigh[first], sleigh[second] = sleigh[second], sleigh[first]
            sleigh = fix_present_position(sleigh)
    return population


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
