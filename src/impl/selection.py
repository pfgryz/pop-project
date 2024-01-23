from random import sample

from src.api.generics import Evaluation
from src.api.igift_manager import IGiftManager
from src.constants import Individual, Population


def tournament_selection(population: Population,
                         evaluation: Evaluation,
                         gift_manager: IGiftManager) -> Individual:
    knights = sample(population, k=2)

    return min(knights, key=lambda k: evaluation(k, gift_manager))
