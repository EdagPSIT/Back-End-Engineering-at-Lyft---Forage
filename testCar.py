import unittest
from datetime import datetime
from tire import *
from carFactory import CarFactory


#tire settings
tire_a = [0.9, 0, 0, 0]
tire_b =  [0.8, 0.8, 0.8, 0.8]

#tire_set = [broken CarriganTire, good CarriganTire, broken OctoprimeTire, good OctoprimeTire]
tire_set = [CarriganTire(tire_a),
    CarriganTire(tire_b),
    OctoprimeTire(tire_b),
    OctoprimeTire(tire_a)
    ]

"""
useing orginal 4 test cases for each model + each tire status
    1) battery & carrigan should be serviced
    2) battery & carrigan should not be serviced
    3) engine & octoprime should be serviced
    4) engine & octoprime should not be serviced
"""

class TestCalliope(unittest.TestCase):

    def test_battery_carrigan_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire_set[0])
        self.assertTrue(car.needs_service())
        self.assertTrue(car.tire.needs_service())
    
    def test_battery_carrigan_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(today,last_service_date, current_mileage, last_service_mileage, tire_set[1])
        self.assertFalse(car.needs_service())

    def test_engine_octoprime_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(today,last_service_date, current_mileage, last_service_mileage, tire_set[2])
        self.assertTrue(car.needs_service())

    def test_engine_octoprime_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_calliope(today,last_service_date, current_mileage, last_service_mileage, tire_set[3])
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_carrigan_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_set[0])
        self.assertTrue(car.needs_service())

    def test_battery_carrigan_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(today,last_service_date, current_mileage, last_service_mileage, tire_set[1])
        self.assertFalse(car.needs_service())

    def test_engine_octoprime_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_glissade(today,last_service_date, current_mileage, last_service_mileage, tire_set[2])
        self.assertTrue(car.needs_service())

    def test_engine_octoprime_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_glissade(today,last_service_date, current_mileage, last_service_mileage, tire_set[3])
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_carrigan_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on, tire_set[0])
        self.assertTrue(car.needs_service())

    def test_battery_carrigan_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on, tire_set[1])
        self.assertFalse(car.needs_service())

    def test_engine_octoprime_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on, tire_set[2])
        self.assertTrue(car.needs_service())

    def test_engine_octoprime_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on, tire_set[3])
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_carrigan_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_set[0])
        self.assertTrue(car.needs_service())

    def test_battery_carrigan_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage, tire_set[1])
        self.assertFalse(car.needs_service())

    def test_engine_octoprime_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage, tire_set[2])
        self.assertTrue(car.needs_service())

    def test_engine_octoprime_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage, tire_set[3])
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_carrigan_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_set[0])
        self.assertTrue(car.needs_service())

    def test_battery_carrigan_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_mileage, tire_set[1])
        self.assertFalse(car.needs_service())

    def test_engine_octoprime_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_mileage, tire_set[2])
        self.assertTrue(car.needs_service())

    def test_engine_octoprime_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_mileage, tire_set[3])
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
