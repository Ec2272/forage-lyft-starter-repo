from abc import ABC, abstractmethod

from test.Servicable import servicable
from car import Car

class Battery(ABC):
    
    def __init__(self, battery, engine,):
        self.battery = Car(battery)
        self.engine = Car(engine)
        

    @abstractmethod
    def needs_service(self):
        pass
