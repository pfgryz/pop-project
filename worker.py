import argparse
import logging
import random
import time

from src.api.generics import Mutation, Generation
from src.data import GiftManager
from src.evolutionary import evolutionary_algorithm
from src.impl.evaluation import cumulative_weighted_reindeer_weariness
from src.impl.generation import gaussian_generation, single_gift_generation, \
    uniform_generation
from src.impl.mutation import random_gift_mutation, last_gift_mutation
from src.impl.selection import tournament_selection


def main(name: str, generation: Generation, mutation: Mutation,
         mutation_probability: float,
         mutation_count: int, iterations: int, seed: int, dataset: str,
         population_size: int, individual_size: int):
    log_format = logging.Formatter("%(message)s")
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    root_logger.addHandler(console_handler)

    file_handler = logging.FileHandler(f"experiments/{name}.log")
    file_handler.setFormatter(log_format)
    root_logger.addHandler(file_handler)

    s = time.time()

    # region Config

    random.seed(seed)
    gm = GiftManager.create_from_file(f"data/{dataset}")
    root_logger.info("BEGIN_EXPERIMENT")

    # endregion

    # region Run

    evolutionary_algorithm(
        gm,
        generation,
        cumulative_weighted_reindeer_weariness,
        tournament_selection,
        mutation,
        individual_size,
        population_size,
        iterations,
        mutation_count=mutation_count,
        mutation_probability=mutation_probability
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
    parser = argparse.ArgumentParser(description="POP Worker")

    parser.add_argument("name", type=str, help="Result filename")
    parser.add_argument("generation", type=str,
                        choices=["single", "uniform", "gaussian"],
                        help="Population generation method")
    parser.add_argument("mutation", type=str,
                        choices=["random", "last"], help="Mutation method")
    parser.add_argument("--mutation_probability", type=float,
                        default=1.0, help="Probability of mutating")
    parser.add_argument("--mutation_count", type=int, default=1,
                        help="Count of mutations")
    parser.add_argument("--iterations", type=int, default=1000,
                        help="Number of iterations")
    parser.add_argument("--seed", type=int, default=100, help="Random seed")
    parser.add_argument("--dataset", type=str,
                        choices=["1000", "10000", "25000"], default="1000",
                        help="Dataset")
    parser.add_argument("--population_size", type=int, default=10,
                        help="Population size")
    parser.add_argument("--individual_size", type=int, default=35,
                        help="Individual size")

    args = parser.parse_args()

    print(args.name, args.generation, args.mutation, args.mutation_probability,
          args.mutation_count, args.iterations, args.seed)

    main(
        args.name,
        single_gift_generation if args.generation == "single" else (
            uniform_generation if args.generation == "uniform" else
            gaussian_generation
        ),
        random_gift_mutation if args.mutation == "random" else last_gift_mutation,
        args.mutation_probability,
        args.mutation_count,
        args.iterations,
        args.seed,
        f"gifts{args.dataset}.csv",
        args.population_size,
        args.individual_size
    )
