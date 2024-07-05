# In engine.py
class Engine(Serviceable):
    def __init__(self):
        self.last_service_mileage = 0
        self.current_mileage = 0

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > self.service_interval

class CapuletEngine(Engine):
    service_interval = 30000

class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool):
        super().__init__()
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on
