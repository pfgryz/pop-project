from src.impl.evaluation import cumulative_weighted_reindeer_weariness
from src.impl.selection import tournament_selection
from tests.impl.common import mock_simple_population


def test_tournament_selection():
    population, gift_manager = mock_simple_population()
    individual_1, _ = population

    individual = tournament_selection(population,
                                      cumulative_weighted_reindeer_weariness,
                                      gift_manager)

    assert individual == individual_1
    assert cumulative_weighted_reindeer_weariness(individual, gift_manager) == \
           cumulative_weighted_reindeer_weariness(individual_1, gift_manager)
