from service import Serviceable
from battery import Battery
from engine import Engine

class Car(Serviceable):
    def __init__(self, Engine, Battery, Tire):
        self.engine = Engine
        self.battery = Battery
        self.tire = Tire

    def needs_service(self) -> bool:
        Flag = False
        print("======")
        if self.engine.needs_service():
            print("Engine needs Service!")
            Flag = True
        if self.battery.needs_service():
            print("Battery needs Service!")
            Flag = True
        
        if self.tire.needs_service():
            print("Tires need Service!")
            Flag = True
        
        if Flag == False:
            print("Service is not required!")
        print("======")
        return Flag


