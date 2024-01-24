from typing import TypeVar

from src.matrix import Matrix

T = TypeVar("T")


class SleighMatrix(Matrix[T]):

    def __init__(self, content: [] = None, wrw: float = 0):
        super().__init__(content)
        self._wrw = wrw

    @property
    def wrw(self) -> float:
        return self._wrw

    def update(self, evaluation, gift_manager: 'IGiftManager'):
        self._wrw = evaluation(self, gift_manager)

    def copy(self) -> 'SleighMatrix':
        return SleighMatrix([element for element in self], self._wrw)
