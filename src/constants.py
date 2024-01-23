from typing import List, Tuple, Callable, TypeVar

from src.utils import Point
from src.matrix import Matrix

# Constants
NorthPole: Point = (90, 0)
BaseWeight: float = 10

# Domain specific
Weight = float
Gift = Tuple[Weight, Point]

GiftId = int
Sleigh = Matrix[GiftId]
Individual = List[Sleigh]
Population = List[Individual]
