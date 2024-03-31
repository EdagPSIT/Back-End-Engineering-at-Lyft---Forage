from service import Serviceable
from battery import Battery
from engine import Engine

class Car(Serviceable):
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery

    def needs_service(self) -> bool:
        if self.engine.needs_service():
            print("Engine needs Service!")
            return True
        if self.battery.needs_service():
            print("Battery needs Service!")
            return True
        
        print("Service is not required!")
        return False


