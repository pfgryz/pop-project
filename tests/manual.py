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

# @todo: WYTWARZANIE
# @todo: przeprowadzić dalsze profilowanie

# @todo: EKSPERYMENTY (FRAMEWORK)
# @todo: przygotować zestaw uruchamiający eksperymenty i zapisujące dane
# @todo:    przydatne do łatwego przetwarzania
# @todo:    format [iteracja - best_in_iter - best_global - ewaluacje]
# @todo: ustawić ziarno dla wszystkich eksperymentów

# @todo: EKSPERYMENTY (WYKONANIE)
# @todo: Eksperymenty 2 x 3 (2 warianty x 3 metody generowania populacji)

# @todo: EKSPERYMENTY (PRZETWARZANIE)
# @todo: wygenerować krzywe zbieżności
# @todo: wygenerować krzywe ECDF (ustalić arbitralny próg)

# @todo: UMOŻLIWE USPRAWNIENIA
# @todo: zamienić prawdopodobieństwo mutacji na skalę mutacji tj. ile
# @todo:    sań ma być zmutowanych w ramach jednego osobnika - zbyt wolno zbiega

# @todo: WSTĘPNE OBSERWACJE
# @todo: uniform - losuje na start dość dobry wynik, ale ciężko go poprawić
# @todo: single - na starcie słabo, ale ciągle się poprawia
# @todo: gaussian - losuje na start dość dobry wynik (podobny do uniform), ale łatwiej poprawia rezultat
