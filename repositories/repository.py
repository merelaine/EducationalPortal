from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, item):
        raise NotImplementedError

    @abstractmethod
    def remove(self, item):
        raise NotImplementedError

    @abstractmethod
    def get(self, item):
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def update(self, item):
        raise NotImplementedError