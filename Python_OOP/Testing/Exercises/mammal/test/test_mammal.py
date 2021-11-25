import sys
sys.path.append(".")

from unittest import TestCase, main
from project.mammal import Mammal

class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal(name="Ceko", mammal_type="Dog", sound="Bau-Bau")

    def test_constructor(self):
        self.assertEqual("Ceko", self.mammal.name)
        self.assertEqual("Dog", self.mammal.type)
        self.assertEqual("Bau-Bau", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)
    
    def test_make_sound(self):
        sound = self.mammal.make_sound()
        self.assertEqual("Ceko makes Bau-Bau", sound)
    
    def test_get_kingdom_method(self):
        kingdom = self.mammal.get_kingdom()
        self.assertEqual("animals", kingdom)

    def test_info_method(self):
        info = self.mammal.info()
        self.assertEqual("Ceko is of type Dog", info)
if __name__ == "__main__":
    main()
