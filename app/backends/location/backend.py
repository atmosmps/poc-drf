from abc import ABCMeta, abstractmethod

from requests import sessions


class LocationBackend(metaclass=ABCMeta):
    @abstractmethod
    def get_data_from_my_ip(self) -> sessions.Session:
        ...
