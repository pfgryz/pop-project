from abc import abstractmethod

from src.model import Gift


class IGiftManager:
    @abstractmethod
    def get_gift(self, index: int) -> Gift:
        pass
