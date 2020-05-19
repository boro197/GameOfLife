from abc import ABC, abstractmethod


class AbstractController(ABC):
    def __init__(self, model):
        self._model = model

    @abstractmethod
    def init_model(self):
        pass
