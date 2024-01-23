from src.impl.evaluation import cumulative_weighted_reindeer_weariness
from src.constants import Individual
from src.impl.selection import tournament_selection
from src.matrix import Matrix
from tests.impl.common import mock_gift_manager, SimpleGiftManager


def test_tournament_selection():
    gift_manager = SimpleGiftManager([
        (13, (69.9496, -17.0366)),
        (5, (-45.1354, 54.6312))
    ])

    individual_1: Individual = [
        Matrix([0, 1])
    ]

    individual_2: Individual = [
        Matrix([0]),
        Matrix([1])
    ]

    individual = tournament_selection([individual_1, individual_2],
                                      cumulative_weighted_reindeer_weariness,
                                      gift_manager)

    assert individual == individual_1
    assert cumulative_weighted_reindeer_weariness(individual, gift_manager) == \
           cumulative_weighted_reindeer_weariness(individual_1, gift_manager)
