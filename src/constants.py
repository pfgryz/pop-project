from typing import List, Tuple, Callable, TypeVar

from src.helpers import Point
from src.sparse_matrix import SparseMatrix

# Constants
NorthPole: Point = (90, 0)
BaseWeight: float = 10

# Domain specific
Weight = float
Gift = Tuple[Weight, Point]

GiftId = int
Sleigh = SparseMatrix[GiftId]
Population = List[Sleigh]
