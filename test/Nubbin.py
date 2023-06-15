from datetime import datetime
from abc import ABC, abstractmethod

from test.Servicable import servicable
from car import Car
from Battery import Battery

class NubbinBattery (Battery):
    def __init__(self, battery, engine, service_date, current date):
        self.battery = Car(battery)
        self.engine = Car(engine)
        self.service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        self.service_date = self.last_service_date.
        self.current_date = datetime.today().date()


    @abstractmethod
    def needs_service(self):
        pass
