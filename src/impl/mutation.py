from copy import deepcopy
from random import sample, uniform, randint

from src.api.igift_manager import IGiftManager
from src.constants import Individual, Population
from src.impl.evaluation import weighted_reindeer_weariness


def last_gift_mutation(individual: Individual,
                       probability: float,
                       gift_manager: IGiftManager) -> Individual:
    # result = deepcopy(individual)
    result = [sleigh.copy() for sleigh in individual]

    if uniform(0, 1) > probability:
        return result

    # Select two sleights
    sleighs = sample(result, k=2)

    # Move gifts from second to first
    if len(sleighs[1]) >= 1:
        sleighs[0].add(sleighs[1][-1])
        sleighs[1].remove(len(sleighs[1]) - 1)
        sleighs[0].update(weighted_reindeer_weariness, gift_manager)
        sleighs[1].update(weighted_reindeer_weariness, gift_manager)

    return result


def random_gift_mutation(individual: Individual,
                         probability: float,
                         gift_manager: IGiftManager) -> Individual:
    # result = deepcopy(individual)
    result = [sleigh.copy() for sleigh in individual]

    if uniform(0, 1) > probability:
        return result

    # Select two sleights
    sleighs = sample(result, k=2)

    # Move gifts from second to first
    if len(sleighs[1]) >= 1:
        position_from = randint(0, len(sleighs[1]) - 1)
        position_to = randint(0, len(sleighs[0]))
        sleighs[0].insert(position_to, sleighs[1][position_from])
        sleighs[1].remove(position_from)
        sleighs[0].update(weighted_reindeer_weariness, gift_manager)
        sleighs[1].update(weighted_reindeer_weariness, gift_manager)

    return result
