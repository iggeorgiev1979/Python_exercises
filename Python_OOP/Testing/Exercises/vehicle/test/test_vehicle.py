import sys
sys.path.append(".")
from project.vehicle import Vehicle
from unittest import TestCase, main

class TestVehicle(TestCase):
    def setUp(self):
        self.car = Vehicle(fuel=50, horse_power=120)
    
    def test_constructor(self):
        self.assertEqual(50, self.car.fuel)
        self.assertEqual(50, self.car.capacity)
        self.assertEqual(120, self.car.horse_power)
        # self.assertEqual(1.25, self.car.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(1.25, self.car.fuel_consumption)
    
    def test_drive_method(self):
        self.car.drive(10)
        self.assertEqual(37.5, self.car.fuel)

    def test_drive_method_with_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))
    
    def test_refuel_method(self):
        self.car.fuel = 30
        self.car.refuel(15)
        self.assertEqual(45, self.car.fuel)
    
    def test_refuel_method_with_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(30)
        self.assertEqual("Too much fuel", str(ex.exception))
    
    def test_str_method(self):
        msg = "The vehicle has 120 horse power with 50 fuel left and 1.25 fuel consumption"
        self.assertEqual(msg, self.car.__str__())

    
if __name__ == "__main__":
    main()
