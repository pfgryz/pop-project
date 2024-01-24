from typing import Callable

from src.api.igift_manager import IGiftManager
from src.constants import Individual, Population

IndividualSize = int
Generation = Callable[[IndividualSize, IGiftManager], Individual]
Evaluation = Callable[[Individual, IGiftManager], float]
Selection = Callable[[Population, Evaluation, IGiftManager], Individual]
Mutation = Callable[[Individual, float, IGiftManager, int], Individual]
