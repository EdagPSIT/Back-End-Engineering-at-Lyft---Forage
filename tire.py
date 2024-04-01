from abc import ABC, abstractmethod
from service import Serviceable

class Tire(Serviceable):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class CarriganTire(Tire):
    def __init__(self, sensors:list[float]):
        self.sensors = sensors
        
    def needs_service(self) -> bool:
        for s in self.sensors:
            if s >= 0.9:
                return True
        else:
            return False
    
class OctoprimeTire(Tire):
    def __init__(self, sensors:list[float]):
        self.sensors = sensors

    def needs_service(self) -> bool:
        total = 0
        for s in self.sensors:
            total += s
        if total >= 3:
            return True
        else:
            return False  
