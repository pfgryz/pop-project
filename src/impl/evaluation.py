from src.api.igift_manager import IGiftManager
from src.constants import Sleigh, NorthPole, BaseWeight, Individual
from src.utils import haversine, counter


def weighted_reindeer_weariness(sleigh: Sleigh, gift_manager: IGiftManager):
    result: float = 0
    previous = None

    if len(sleigh) == 0:
        return 0

    for position, gift in enumerate(sleigh):
        # Choose starting point
        if result == 0:
            start_point = NorthPole
        else:
            _, start_point = gift_manager.get_gift(previous)

        # Get end point and calculate distance between
        _, end_point = gift_manager.get_gift(gift)
        distance = haversine(start_point, end_point)

        # Calculate weight
        cumulative_weight = BaseWeight
        for gift_to_move in sleigh[position:]:
            weight, _ = gift_manager.get_gift(gift_to_move)
            cumulative_weight += weight

        # Sum result
        result += cumulative_weight * distance

        # Save previous gift
        previous = gift

    _, start_point = gift_manager.get_gift(previous)
    result += BaseWeight * haversine(start_point, NorthPole)

    return result


@counter
def cumulative_weighted_reindeer_weariness(individual: Individual,
                                           gift_manager: IGiftManager) -> float:
    return sum(sleigh.wrw for sleigh in
               individual)
