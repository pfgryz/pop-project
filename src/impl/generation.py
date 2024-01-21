from math import floor
from random import choice, randint, uniform, gauss
from typing import List

from src.api.igift_manager import IGiftManager
from src.constants import Population, Sleigh
from src.sparse_matrix import SparseMatrixHelpers


def generate_population_single_gift(population_size: int,
                                    gift_manager: IGiftManager) -> Population:
    population: Population = []
    gifts = list(range(gift_manager.get_count()))

    for index in range(gift_manager.get_count()):
        gift = choice(gifts)
        gifts.remove(gift)
        sleigh: Sleigh = [(0, gift)]
        population.append(sleigh)

    return population


def generate_population_uniform(population_size: int,
                                gift_manager: IGiftManager) -> Population:
    population: Population = []
    gifts = list(range(gift_manager.get_count()))

    for index in range(population_size):
        sleigh: Sleigh = []
        population.append(sleigh)

    while len(gifts) > 0:
        gift = gifts.pop()
        sleigh_id = floor(uniform(0, population_size))

        SparseMatrixHelpers.add(population[sleigh_id], gift)

    return population


def generate_population_gaussian(population_size: int,
                                  gift_manager: IGiftManager) -> Population:
    population: Population = []
    gifts = list(range(gift_manager.get_count()))

    for index in range(population_size):
        sleigh: Sleigh = []
        population.append(sleigh)

    while len(gifts) > 0:
        gift = gifts.pop()

        sleigh_id = -1
        while sleigh_id < 0 or sleigh_id >= population_size:
            sleigh_id = floor(gauss(population_size / 2, population_size / 4))

        SparseMatrixHelpers.add(population[sleigh_id], gift)

    return population
