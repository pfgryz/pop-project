import time

from src.evolutionary import evolutionary_algorithm
from src.impl.evaluation import cumulative_weighted_reindeer_weariness
from src.impl.generation import single_gift_generation, uniform_generation, \
    gaussian_generation
from src.impl.mutation import last_gift_mutation, random_gift_mutation
from src.impl.selection import tournament_selection
from tests.impl.common import mock_gift_manager

if __name__ == "__main__":
    GIFTS = 1000
    s = time.time()
    gm = mock_gift_manager(GIFTS)

    evolutionary_algorithm(
        gm,
        gaussian_generation,
        cumulative_weighted_reindeer_weariness,
        tournament_selection,
        random_gift_mutation,
        30,
        10,
        100
    )

    e = time.time()
    print((e - s))
    print(cumulative_weighted_reindeer_weariness.counter)

# @todo: EKSPERYMENTY (PRZETWARZANIE)
# @todo: wygenerować krzywe zbieżności
# @todo: wygenerować krzywe ECDF (ustalić arbitralny próg)

# @todo: WSTĘPNE OBSERWACJE
# @todo: uniform - losuje na start dość dobry wynik, ale ciężko go poprawić
# @todo: single - na starcie słabo, ale ciągle się poprawia
# @todo: gaussian - losuje na start dość dobry wynik (podobny do uniform), ale łatwiej poprawia rezultat
