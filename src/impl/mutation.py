from copy import deepcopy
from random import sample

from src.constants import Individual, Population


def mutation_move_last(population: Population,
                       probability: float) -> Individual:
    # Select two individuals
    individuals = sample(population, k=2)

    # Copy the target
    result = deepcopy(individuals[0])
