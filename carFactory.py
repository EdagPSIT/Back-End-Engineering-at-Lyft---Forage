from car import Car
from engine import *
from battery import *
from tire import *
from datetime import date

class CarFactory():
    
    @staticmethod
    def create_calliope(current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, tire:Tire):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindleBattery(current_date, last_service_date)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_glissade(current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, tire:Tire):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindleBattery(current_date, last_service_date)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_palindrome(current_date:date, last_service_date:date, warning_light_is_on:bool, tire:Tire):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindleBattery(current_date, last_service_date)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_rorschach(current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, tire:Tire):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_thovex(current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, tire: Tire):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery, tire)
    
