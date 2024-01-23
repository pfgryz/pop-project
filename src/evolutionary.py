from copy import deepcopy

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

    individual = deepcopy(individual)
    return individual, rating


def evolutionary_algorithm(
        gift_manager: IGiftManager,
        generation: Generation,
        evaluation: Evaluation,
        selection: Selection,
        mutation: Mutation,
        individual_size: int,
        population_size: int,
        iterations: int
):
    population = [
        generation(individual_size, gift_manager)
        for _ in range(population_size)
    ]

    t = 1
    log = [select_best(population, evaluation, gift_manager)]

    while t < iterations:
        print(f"Iteration: {t + 1}/{iterations} - best: {round(log[-1][1])}")

        succession = []

        for _ in range(population_size):
            individual = selection(population, evaluation, gift_manager)
            mutated = mutation(individual, 0.5)
            succession.append(mutated)

        log.append(
            select_best(succession, evaluation, gift_manager)
        )

        population = succession

        t += 1

    for result in log:
        print(result[1])
