from typing import List, Tuple, Callable, TypeVar

from src.utils import Point
from src.sleigh_matrix import SleighMatrix

# Constants
NorthPole: Point = (90, 0)
BaseWeight: float = 10
MaxWeight: float = 1000

# Domain specific
Weight = float
Gift = Tuple[Weight, Point]

GiftId = int
Sleigh = SleighMatrix[GiftId]
Individual = List[Sleigh]
Population = List[Individual]
