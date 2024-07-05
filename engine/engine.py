from serviceable import Serviceable

class Engine(Serviceable):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

class CapuletEngine(Engine):
    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 30000

class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on

class WilloughbyEngine(Engine):
    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 60000
