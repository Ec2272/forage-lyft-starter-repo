from abc import ABC, abstractmethod
from test.Servicable import servicable


class Car(ABC):
    def __init__(self, battery, engine,):
        self.battery = battery
        self.engine = engine


    @abstractmethod
    def needs_service(self):
        pass
