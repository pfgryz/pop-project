from src.evolutionary import evolutionary_algorithm
from src.impl.evaluation import cumulative_weighted_reindeer_weariness
from src.impl.generation import single_gift_generation, uniform_generation
from src.impl.mutation import last_gift_mutation, random_gift_mutation
from src.impl.selection import tournament_selection
from tests.impl.common import mock_gift_manager

if __name__ == "__main__":
    GIFTS = 1000

    gm = mock_gift_manager(GIFTS)

    evolutionary_algorithm(
        gm,
        uniform_generation,
        cumulative_weighted_reindeer_weariness,
        tournament_selection,
        random_gift_mutation,
        30,
        2,
        1000
    )
