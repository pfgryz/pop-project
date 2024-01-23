from typing import List

from src.constants import Gift
from src.api.igift_manager import IGiftManager


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
