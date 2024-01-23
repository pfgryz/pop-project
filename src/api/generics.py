from typing import Callable

from src.constants import Individual, Population

from src.api.igift_manager import IGiftManager

PopulationSize = int
Generation = Callable[[PopulationSize, IGiftManager], Individual]
Evaluation = Callable[[Individual, IGiftManager], float]
Selection = Callable[[Population, Evaluation, IGiftManager], Individual]
