"""Module data serializer"""

from abc import ABC, abstractmethod


class DataSerializer(ABC):
    @abstractmethod
    def serialize(self, data: dict):
        pass
