from car_manager import Car
from unittest import TestCase, main

class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Ford", "Focus", 7, 50)

    def test_the_constructor(self):
        self.assertEqual("Ford", self.car.make)
        self.assertEqual("Focus", self.car.model)
        self.assertEqual(7, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)
    
    def test_car_make(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "Focus", fuel_consumption=7, fuel_capacity=50)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))
    
    def test_car_model(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Ford", "", fuel_consumption=7, fuel_capacity=50)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))
    
    def test_car_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Ford", "Focus", fuel_consumption=0, fuel_capacity=50)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))
    
    def test_car_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Ford", "Focus", fuel_consumption=7, fuel_capacity=0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))
    
    def test_car_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))
    
    def test_refuel_method(self):
        self.car.refuel(60)
        self.assertEqual(50, self.car.fuel_amount)
    
    def test_refuel_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-20)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
    
    def test_drive_method_with_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
    
    def test_drive_method(self):
        self.car.drive(0)
        self.assertEqual(0, self.car.fuel_amount)
        
if __name__ == "__main__":
    main()
