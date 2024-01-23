from math import floor
from random import choice, randint, uniform, gauss

from src.api.igift_manager import IGiftManager
from src.constants import Individual, Sleigh
from src.matrix import Matrix


def single_gift_generation(individual_size: int,
                           gift_manager: IGiftManager) -> Individual:
    population: Individual = []
    gifts = list(range(gift_manager.get_count()))

    for index in range(gift_manager.get_count()):
        gift = choice(gifts)
        gifts.remove(gift)
        sleigh: Sleigh = Matrix([gift])
        population.append(sleigh)

    return population


def uniform_generation(individual_size: int,
                       gift_manager: IGiftManager) -> Individual:
    population: Individual = []
    gifts = list(range(gift_manager.get_count()))

    for index in range(individual_size):
        sleigh: Sleigh = Matrix([])
        population.append(sleigh)

    while len(gifts) > 0:
        gift = gifts.pop()
        sleigh_id = floor(uniform(0, individual_size))

        population[sleigh_id].add(gift)

    return population


def gaussian_generation(individual_size: int,
                        gift_manager: IGiftManager) -> Individual:
    population: Individual = []
    gifts = list(range(gift_manager.get_count()))

    for index in range(individual_size):
        sleigh: Sleigh = Matrix([])
        population.append(sleigh)

    while len(gifts) > 0:
        gift = gifts.pop()

        sleigh_id = -1
        while sleigh_id < 0 or sleigh_id >= individual_size:
            sleigh_id = floor(gauss(individual_size / 2, individual_size / 4))

        population[sleigh_id].add(gift)

    return population
