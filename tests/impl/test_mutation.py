from random import seed

from src.impl.mutation import last_gift_mutation, random_gift_mutation
from tests.impl.common import mock_simple_population


def test_last_gift_mutation_first():
    population, gift_manager = mock_simple_population()

    _, individual_2 = population

    seed(100)
    result = last_gift_mutation(individual_2, 0.2, gift_manager)

    assert len(result[0]) == 0
    assert len(result[1]) == 2


def test_last_gift_mutation_second():
    population, gift_manager = mock_simple_population()

    _, individual_2 = population

    seed(120)
    result = last_gift_mutation(individual_2, 0.6, gift_manager)

    assert len(result[0]) == 2
    assert len(result[1]) == 0


def test_last_gift_mutation_not_mutated():
    population, gift_manager = mock_simple_population()

    _, individual_2 = population

    seed(100)
    result = last_gift_mutation(individual_2, 0.1, gift_manager)

    assert len(result[0]) == 1
    assert len(result[1]) == 1


def test_random_gift_mutation():
    population, gift_manager = mock_simple_population()

    _, individual_2 = population

    seed(100)
    result = random_gift_mutation(individual_2, 0.2, gift_manager)

    assert len(result[0]) == 0
    assert len(result[1]) == 2
    assert result[1][0] == 1
    assert result[1][1] == 0


def test_random_gift_mutation_other():
    population, gift_manager = mock_simple_population()

    _, individual_2 = population

    seed(120)
    result = random_gift_mutation(individual_2, 0.6, gift_manager)

    assert len(result[0]) == 2
    assert len(result[1]) == 0
    assert result[0][0] == 0
    assert result[0][1] == 1
