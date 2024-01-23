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


def tournament_selection(population, tournament_size, tournament_function,
                         evaluation, probability):
    all_winners = []
    for _ in range(tournament_size):
        winners = tournament_function(deepcopy(population), evaluation,
                                      probability)
        for winner in winners:
            all_winners.append(winner)
    return all_winners


def tournament_2(population, evaluation, probability):
    shuffle(population)
    new_population = []
    i = 0
    while i < len(population):
        if evaluation(population[i]) < evaluation(population[i + 1]):
            better_id = i
            worse_id = i + 1
        else:
            better_id = i + 1
            worse_id = i
        if np.random.uniform() < probability:
            new_population.append(population[better_id])
        else:
            new_population.append(population[worse_id])
        i += 2
    return new_population


def fix_present_position(sleigh):
    for i in range(len(sleigh)):
        gift_id, _ = sleigh[i]
        sleigh[i] = (gift_id, i)
    return sleigh


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


def population_one_gift_in_sleigh(population_size, number_of_populations):
    populations = []
    for _ in range(number_of_populations):
        population = []
        gifts_id = [i for i in range(len(DATA))]
        for _ in range(population_size):
            sleigh = []
            chosen_gift_id = choice(gifts_id)
            gifts_id.remove(chosen_gift_id)
            sleigh.append((chosen_gift_id, 0))
            population.append(sleigh)
        populations.append(population)
    return populations


def population_uniform(population_size, number_of_populations):
    populations = []
    for _ in range(number_of_populations):
        population = []
        gifts_per_sleigh = len(DATA) // population_size
        gifts_id = [i for i in range(len(DATA))]
        for _ in range(population_size):
            sleigh = []
            for i in range(gifts_per_sleigh):
                chosen_gift_id = choice(gifts_id)
                gifts_id.remove(chosen_gift_id)
                sleigh.append((chosen_gift_id, i))
            population.append(sleigh)
        if len(gifts_id) > 0:
            for gift_id in gifts_id:
                chosen_sleigh = randint(0, len(population) - 1)
                population[chosen_sleigh].append(
                    (gift_id, len(population[chosen_sleigh])))
        populations.append(population)
    return populations


def population_gaussian(population_size, number_of_populations):
    populations = []
    for _ in range(number_of_populations):
        population = []
        # powiem tak, chyba tutaj wolę nie tworzyć żadnych herezji...
        populations.append(population)
    return populations


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
