from typing import Callable

from src.constants import Population

from src.api.igift_manager import IGiftManager

PopulationSize = int
Generation = Callable[[PopulationSize, IGiftManager], Population]
