from typing import List, Tuple

from src.constants import Gift, Population, Individual
from src.api.igift_manager import IGiftManager
from src.matrix import Matrix
from src.sleigh_matrix import SleighMatrix


class SimpleGiftManager(IGiftManager):

    def __init__(self, gifts: List[Gift]):
        self.gifts = gifts

    def get_gift(self, index: int) -> Gift:
        return self.gifts[index]

    def get_count(self) -> int:
        return len(self.gifts)


def mock_gift_manager(gifts_amount: int) -> IGiftManager:
    return SimpleGiftManager([
        (index, (1 / (1 + index), 1)) for index in range(gifts_amount)
    ])


def mock_simple_population() -> Tuple[Population, IGiftManager]:
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

    return [individual_1, individual_2], gift_manager
