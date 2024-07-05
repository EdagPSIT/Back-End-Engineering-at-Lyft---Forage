from datetime import date
from car import Car
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import SpindlerBattery, NubbinBattery

class CarFactory:
    @staticmethod
    def create_calliope(current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(date.today(), date.today())
        return Car(engine, battery)

    # Additional methods for other car models...
