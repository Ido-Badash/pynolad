from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def run(self, dt: float):
        """Runs the state"""
        pass
