from abc import abstractmethod
from abc import ABCMeta


class Device(metaclass=ABCMeta):
    @property
    def is_on(self):
        raise NotImplementedError

    @abstractmethod
    def is_enable(self):
        raise NotImplementedError

    @abstractmethod
    def enable(self):
        raise NotImplementedError

    @abstractmethod
    def disable(self):
        raise NotImplementedError

    @abstractmethod
    def get_volumen(self):
        raise NotImplementedError

    @abstractmethod
    def set_volumen(self, percent: int):
        raise NotImplementedError

    @abstractmethod
    def get_channel(self):
        raise NotImplementedError

    @abstractmethod
    def set_channel(self, channel: int):
        raise NotImplementedError
