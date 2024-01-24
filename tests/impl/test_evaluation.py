from pytest import approx

from src.constants import Individual
from src.impl.evaluation import weighted_reindeer_weariness, \
    cumulative_weighted_reindeer_weariness
from src.sleigh_matrix import SleighMatrix
from tests.impl.common import SimpleGiftManager


def test_wrs_for_empty_sleigh():
    assert weighted_reindeer_weariness(SleighMatrix(),
                                       SimpleGiftManager([])) == 0


def test_wrs_for_single_gift_without_weight():
    gift_manager = SimpleGiftManager([(0, (69.9496, -17.0366))])
    assert weighted_reindeer_weariness(SleighMatrix([0]), gift_manager) == \
           approx(44590, abs=0.1)


def test_wrs_for_single_gift():
    gift_manager = SimpleGiftManager([(13, (69.9496, -17.0366))])
    assert weighted_reindeer_weariness(SleighMatrix([0]), gift_manager) == \
           approx(73573.5, abs=0.1)


def test_wrs_for_two_gifts():
    gift_manager = SimpleGiftManager([
        (13, (69.9496, -17.0366)),
        (5, (-45.1354, 54.6312))
    ])
    assert weighted_reindeer_weariness(SleighMatrix([0, 1]),
                                       gift_manager) == approx(
        423080.2, abs=0.1)


def test_cumulative_wrs_for_two_sleighs():
    gift_manager = SimpleGiftManager([
        (13, (69.9496, -17.0366)),
        (5, (-45.1354, 54.6312))
    ])

    individual = [
        SleighMatrix([0, 1]),
        SleighMatrix([0])
    ]

    for sleigh in individual:
        sleigh.update(weighted_reindeer_weariness, gift_manager)

    assert cumulative_weighted_reindeer_weariness(
        individual,
        gift_manager
    ) == approx(496653.7, abs=0.2)


def test_evaluation_for_two_individuals():
    gift_manager = SimpleGiftManager([
        (13, (69.9496, -17.0366)),
        (5, (-45.1354, 54.6312))
    ])

    individual_1: Individual = [
        SleighMatrix([0, 1])
    ]

    individual_2: Individual = [
        SleighMatrix([0]),
        SleighMatrix([1])
    ]

    for sleigh in individual_1:
        sleigh.update(weighted_reindeer_weariness, gift_manager)

    for sleigh in individual_2:
        sleigh.update(weighted_reindeer_weariness, gift_manager)

    assert cumulative_weighted_reindeer_weariness(individual_1, gift_manager) \
           == approx(423080.2, abs=0.1)
    assert cumulative_weighted_reindeer_weariness(individual_2, gift_manager) \
           == approx(449232.8, abs=0.1)
