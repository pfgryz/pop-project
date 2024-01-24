import logging
import random
import time

from src.evolutionary import evolutionary_algorithm
from src.impl.evaluation import cumulative_weighted_reindeer_weariness
from src.impl.generation import gaussian_generation
from src.impl.mutation import random_gift_mutation
from src.impl.selection import tournament_selection
from tests.impl.common import mock_gift_manager


def main():
    log_format = logging.Formatter("%(message)s")
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    root_logger.addHandler(console_handler)

    file_handler = logging.FileHandler(f"gaussian.log")
    file_handler.setFormatter(log_format)
    root_logger.addHandler(file_handler)

    # region Config
    seed = 100
    GIFTS = 1000
    s = time.time()
    random.seed(seed)
    gm = mock_gift_manager(GIFTS)

    root_logger.info("BEGIN_EXPERIMENT")

    # endregion

    # region Run

    evolutionary_algorithm(
        gm,
        gaussian_generation,
        cumulative_weighted_reindeer_weariness,
        tournament_selection,
        random_gift_mutation,
        35,
        10,
        1000,
        mutation_count=10,
        mutation_probability=1
    )

    # endregion

    root_logger.info("END_EXPERIMENT")
    root_logger.info("BEGIN_STATISTICS")

    e = time.time()
    elapsed_time = e - s
    root_logger.info(elapsed_time)
    root_logger.info(cumulative_weighted_reindeer_weariness.counter)
    root_logger.info(seed)

    root_logger.info("END_STATISTICS")


if __name__ == "__main__":
    main()
