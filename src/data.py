import csv
from typing import List

from src.api.igift_manager import IGiftManager
from src.constants import Gift


class GiftManager(IGiftManager):
    def __init__(self, gifts: List[Gift]):
        self.gifts = gifts

    def get_gift(self, index: int) -> Gift:
        return self.gifts[index]

    def get_count(self) -> int:
        return len(self.gifts)

    @classmethod
    def create_from_file(cls, pathname: str) -> 'GiftManager':
        gifts = []

        with open(pathname, "r") as handle:
            reader = csv.DictReader(handle)

            for row in reader:
                gift = (
                    float(row.get("Weight")), (
                        float(row.get("Latitude")),
                        float(row.get("Longitude"))
                    )
                )
                gifts.append(gift)

        return cls(gifts)
