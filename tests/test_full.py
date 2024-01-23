from src.evolutionary import evolutionary_algorithm
from src.impl.evaluation import cumulative_weighted_reindeer_weariness
from src.impl.generation import single_gift_generation
from src.impl.mutation import last_gift_mutation
from src.impl.selection import tournament_selection
from tests.impl.common import mock_gift_manager


def test_evolutionary_algorithm():

    GIFTS = 100

    gm = mock_gift_manager(GIFTS)

    evolutionary_algorithm(
        gm,
        single_gift_generation,
        cumulative_weighted_reindeer_weariness,
        tournament_selection,
        last_gift_mutation,
        25,
        100,
        100
    )
