from abc import abstractmethod

from src.constants import Gift


class IGiftManager:
    @abstractmethod
    def get_gift(self, index: int) -> Gift:
        pass

    @abstractmethod
    def get_count(self) -> int:
        pass
