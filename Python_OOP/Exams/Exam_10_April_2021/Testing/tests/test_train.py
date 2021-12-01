import sys
sys.path.append(".")
from project.train.train import Train
from unittest import TestCase, main

class TestTrain(TestCase):
    def setUp(self):
        self.train = Train("Orient", 2)
    
    def test_class_attributes(self):
        self.assertEqual("Train is full", Train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", Train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", Train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", Train.PASSENGER_ADD)
        self.assertEqual("Removed {}", Train.PASSENGER_REMOVED)
        self.assertEqual(0, Train.ZERO_CAPACITY)
    
    def test_constructor(self):
        self.assertEqual("Orient", self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertEqual([], self.train.passengers)
    
    def test_add(self):
        self.train.add("Ivan")
        self.train.add("Petar")
        with self.assertRaises(ValueError) as er:
            self.train.add("Kiril")
        self.assertEqual("Train is full", str(er.exception))

        self.train.remove("Petar")
        with self.assertRaises(ValueError) as er:
            self.train.add("Ivan")
        self.assertEqual("Passenger Ivan Exists", str(er.exception))

        msg = self.train.add("Petar")
        self.assertEqual("Added passenger Petar", msg)
        self.assertEqual(["Ivan", "Petar"], self.train.passengers)
    
    def test_remove(self):
        with self.assertRaises(ValueError) as er:
            self.train.remove("Ivan")
        self.assertEqual("Passenger Not Found", str(er.exception))

        self.train.add("Ivan")
        msg = self.train.remove("Ivan")
        self.assertEqual("Removed Ivan", msg)

        self.assertEqual([], self.train.passengers)


if __name__ == "__main__":
    main()
