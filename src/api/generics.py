from typing import Callable

from src.constants import Individual, Population

from src.api.igift_manager import IGiftManager

IndividualSize = int
Generation = Callable[[IndividualSize, IGiftManager], Individual]
Evaluation = Callable[[Individual, IGiftManager], float]
Selection = Callable[[Population, Evaluation, IGiftManager], Individual]
Mutation = Callable[[Individual, float, IGiftManager], Individual]
