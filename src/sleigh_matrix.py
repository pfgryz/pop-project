from typing import TypeVar

from src.matrix import Matrix

T = TypeVar("T")


class SleighMatrix(Matrix[T]):

    def __init__(self, content: [] = None, wrw: float = 0, weight: float = 0):
        super().__init__(content)
        self._wrw = wrw
        self._weight = weight

    @property
    def wrw(self) -> float:
        return self._wrw

    @property
    def weight(self) -> float:
        return self._weight

    def update(self, evaluation, gift_manager: 'IGiftManager'):
        self._wrw = evaluation(self, gift_manager)
        self._weight = 0

        for gift in self:
            self._weight += gift_manager.get_gift(gift)[0]

    def copy(self) -> 'SleighMatrix':
        return SleighMatrix([element for element in self], self._wrw,
                            self._weight)
