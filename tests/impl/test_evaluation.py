from typing import List
from pytest import approx

from src.api.igift_manager import IGiftManager
from src.impl.evaluation import weighted_reindeer_weariness, \
    cumulative_weighted_reindeer_weariness
from src.constants import Gift, Individual
from tests.impl.common import SimpleGiftManager


def test_wrs_for_empty_sleigh():
    assert weighted_reindeer_weariness([], SimpleGiftManager([])) == 0


def test_wrs_for_single_gift_without_weight():
    gift_manager = SimpleGiftManager([(0, (69.9496, -17.0366))])
    assert weighted_reindeer_weariness([(0, 0)], gift_manager) == \
           approx(44590, abs=0.1)


def test_wrs_for_single_gift():
    gift_manager = SimpleGiftManager([(13, (69.9496, -17.0366))])
    assert weighted_reindeer_weariness([(0, 0)], gift_manager) == \
           approx(73573.5, abs=0.1)


def test_wrs_for_two_gifts():
    gift_manager = SimpleGiftManager([
        (13, (69.9496, -17.0366)),
        (5, (-45.1354, 54.6312))
    ])
    assert weighted_reindeer_weariness(
        [(0, 0), (1, 1)], gift_manager) == approx(423080.2, abs=0.1)


def test_cumulative_wrs_for_two_sleighs():
    gift_manager = SimpleGiftManager([
        (13, (69.9496, -17.0366)),
        (5, (-45.1354, 54.6312))
    ])

    assert cumulative_weighted_reindeer_weariness(
        [
            [(0, 0), (1, 1)],
            [(0, 0)]
        ],
        gift_manager
    ) == approx(496653.7, abs=0.2)


def test_evaluation_for_two_individuals():
    gift_manager = SimpleGiftManager([
        (13, (69.9496, -17.0366)),
        (5, (-45.1354, 54.6312))
    ])

    individual_1: Individual = [
        [
            (0, 0),
            (0, 1)
        ]
    ]

    individual_2: Individual = [
        [
            (0, 0)
        ],
        [
            (0, 1)
        ]
    ]

    assert cumulative_weighted_reindeer_weariness(individual_1, gift_manager) \
           == approx(605418.6, abs=0.1)
    assert cumulative_weighted_reindeer_weariness(individual_2, gift_manager) \
           == approx(449232.8, abs=0.1)