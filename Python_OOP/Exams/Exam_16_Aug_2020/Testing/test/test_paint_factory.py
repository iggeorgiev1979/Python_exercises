import sys
sys.path.append(".")
from project.factory.paint_factory import PaintFactory
from unittest import TestCase, main

class TestPaintFactory(TestCase):
    def setUp(self):
        self.factory = PaintFactory("Levis", 20)
    
    def test_constructor(self):
        self.assertEqual("Levis", self.factory.name)
        self.assertEqual(20, self.factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)
        self.assertEqual({}, self.factory.ingredients)
    
    def test_the_property_products(self):
        self.assertEqual({}, self.factory.products)
    
    def test_add_method(self):
        with self.assertRaises(TypeError) as te:
            self.factory.add_ingredient("black", 10)
        self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(te.exception))

        with self.assertRaises(ValueError) as ve:
            self.factory.add_ingredient("white", 30)
        self.assertEqual("Not enough space in factory", str(ve.exception))

        self.factory.add_ingredient("white", 5)
        self.assertEqual({"white": 5}, self.factory.ingredients)
        self.assertEqual({"white": 5}, self.factory.products)
    
    def test_can_add_method(self):
        self.assertEqual(True, self.factory.can_add(5))

        self.assertEqual(False, self.factory.can_add(35))
    
    def test_remove_method(self):
        with self.assertRaises(KeyError) as ke:
            self.factory.remove_ingredient("white", 5)
        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))
        self.factory.add_ingredient("white", 5)
        with self.assertRaises(ValueError) as ve:
            self.factory.remove_ingredient("white", 10)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))
        self.factory.remove_ingredient("white", 3)
        self.assertEqual({"white": 2}, self.factory.ingredients)
        self.assertEqual({"white": 2}, self.factory.products)
    
    def test_repr_method(self):
        self.factory.add_ingredient("white", 10)
        msg = """Factory name: Levis with capacity 20.
white: 10
"""
        self.assertEqual(msg, repr(self.factory))

        


if __name__ == "__main__":
    main()

