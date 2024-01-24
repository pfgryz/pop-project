import logging

from src.api.generics import Generation, Evaluation, Selection, Mutation
from src.api.igift_manager import IGiftManager
from src.constants import Individual, Population


def select_best(population: Population, evaluation: Evaluation,
                gift_manager: IGiftManager) -> [Individual,
                                                float]:
    individual, rating = min(
        [
            (individual,
             evaluation(individual, gift_manager))
            for individual in population
        ], key=lambda pair: pair[1])

    individual = [sleigh.copy() for sleigh in individual]
    return individual, rating


def evolutionary_algorithm(
        gift_manager: IGiftManager,
        generation: Generation,
        evaluation: Evaluation,
        selection: Selection,
        mutation: Mutation,
        individual_size: int,
        population_size: int,
        iterations: int,
        mutation_probability: float = 1,
        mutation_count: int = 1
):
    population = [
        generation(individual_size, gift_manager)
        for _ in range(population_size)
    ]

    logger = logging.getLogger("")

    t = 0
    log = [select_best(population, evaluation, gift_manager)]
    total_best = log[0]

    while t < iterations:
        succession = []

        for _ in range(population_size):
            individual = selection(population, evaluation, gift_manager)
            mutated = mutation(individual, mutation_probability, gift_manager,
                               mutation_count)
            succession.append(mutated)

        best = select_best(succession, evaluation, gift_manager)

        if best[1] < total_best[1]:
            total_best = best

        log.append(best)

        population = succession

        t += 1

        logger.info(
            f"{t}/{iterations} {log[-1][1]} {total_best[1]} - {evaluation.counter}"
        )
