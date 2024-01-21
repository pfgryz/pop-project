from typing import List
import matplotlib.pyplot as plt

from src.api.igift_manager import IGiftManager
from src.constants import Gift
from src.impl.generation import generate_population_single_gift, \
    generate_population_uniform, generate_population_gaussian

GIFTS = 10000


class SimpleGiftManager(IGiftManager):

    def __init__(self, gifts: List[Gift]):
        self.gifts = gifts

    def get_gift(self, index: int) -> Gift:
        return self.gifts[index]

    def get_count(self) -> int:
        return len(self.gifts)


def mock_gift_manager(gifts_amount: int) -> IGiftManager:
    return SimpleGiftManager([
        (index, (1, 1)) for index in range(gifts_amount)
    ])


def test_single():
    population = generate_population_single_gift(GIFTS,
                                                 mock_gift_manager(
                                                     GIFTS))

    x = list(range(GIFTS))
    y = [
        len([sleigh for sleigh in population if len(sleigh) == xi])
        for xi in x
    ]
    plt.plot(x, y)
    plt.title("Single - Sleighs Size")
    plt.xlabel("Sleigh Size")
    plt.ylabel("Amount of Sleighs")
    plt.show()

    y2 = [len(sleigh) for sleigh in population]
    plt.plot(x, y2)
    plt.title("Single - Sleighs")
    plt.xlabel("Sleigh Index")
    plt.ylabel("Size")
    plt.show()


def test_uniform():
    population = generate_population_uniform(100, mock_gift_manager(
        GIFTS))

    x = list(range(GIFTS // 50))
    y = [
        len([sleigh for sleigh in population if len(sleigh) == xi])
        for xi in x
    ]

    plt.plot(x, y)
    plt.title("Uniform - Sleighs Size")
    plt.xlabel("Sleigh Size")
    plt.ylabel("Amount of Sleighs")
    plt.show()

    x2 = list(range(100))
    y2 = [len(sleigh) for sleigh in population]
    plt.plot(x2, y2)
    plt.title("Uniform - Sleighs")
    plt.xlabel("Sleigh Index")
    plt.ylabel("Size")
    plt.show()


def test_gauss():
    population = generate_population_gaussian(100, mock_gift_manager(
        GIFTS))

    x = list(range(GIFTS // 50))
    y = [
        len([sleigh for sleigh in population if len(sleigh) == xi])
        for xi in x
    ]

    plt.plot(x, y)
    plt.title("Gauss - Sleighs Size")
    plt.xlabel("Sleigh Size")
    plt.ylabel("Amount of Sleighs")
    plt.show()

    x2 = list(range(100))
    y2 = [len(sleigh) for sleigh in population]
    plt.plot(x2, y2)
    plt.title("Gauss - Sleighs")
    plt.xlabel("Sleigh Index")
    plt.ylabel("Size")
    plt.show()
