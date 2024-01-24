from typing import TypeVar, Generic

T = TypeVar("T")


class Matrix(Generic[T]):

    def __init__(self, content: [] = None):
        self._content = []

        if content is not None:
            for element in content:
                self.add(element)

    def __len__(self):
        return len(self._content)

    def __getitem__(self, item: int):
        return [element[1] for element in self._content][item]

    def add(self, value: T) -> 'Matrix':
        count = len(self._content)
        self._content.append((count, value))
        return self

    def insert(self, position: int, value: T) -> 'Matrix':
        if position == len(self):
            return self.add(value)

        self._content.insert(position, (position, value))
        for index in range(position, len(self._content)):
            _, value = self._content[index]
            self._content[index] = (index, value)

    def remove(self, position: int) -> 'Matrix':
        if position >= len(self._content) or position < 0:
            raise IndexError("Index out of range")

        self._content.pop(position)

        count = len(self._content)
        for index in range(position, count):
            _, value = self._content[index]
            self._content[index] = (index, value)

        return self

    def validate(self) -> bool:
        count = len(self._content)

        for index in range(count):
            position, _ = self._content[index]

            if position != index:
                return False

        return True

    def sort(self) -> 'Matrix':
        self._content.sort(key=lambda item: item[0])
        return self
