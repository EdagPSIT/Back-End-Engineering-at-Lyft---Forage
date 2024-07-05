from serviceable import Serviceable

class Battery(Serviceable):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

class SpindlerBattery(Battery):
    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days >= 730  # 2 years

class NubbinBattery(Battery):
    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days >= 1460  # 4 years
