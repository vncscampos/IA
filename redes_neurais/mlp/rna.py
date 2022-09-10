from abc import ABC, abstractmethod

class RNA(ABC):
    @abstractmethod
    def training(self, x_in: list, y: list):
        pass

    @abstractmethod
    def exec(self, x_in: list):
        pass