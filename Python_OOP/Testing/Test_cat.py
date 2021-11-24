from cat import Cat
from unittest import TestCase, main

class CatTest(TestCase):
    def test_if_the_cat_size_is_increased_after_eating(self):
        cat = Cat("Test")
        cat.eat()
        self.assertEqual(1, cat.size)

    def test_if_the_cat_is_fed_after_eating(self):
        cat = Cat("Test")
        cat.eat()
        self.assertTrue(cat.fed)
    
    def test_if_the_cat_cannot_eat_when_already_fed(self):
        cat = Cat("Test")
        cat.eat()
        with self.assertRaises(Exception) as ex:
            cat.eat()
        
        self.assertEqual("Already fed.", str(ex.exception))
    
    def test_if_the_cat_cannot_fall_asleep_if_not_fed(self):
        cat = Cat("Test")
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))
    
    def test_if_the_cat_is_not_sleepy_after_sleeping(self):
        cat = Cat("Test")
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)
if __name__ == "__main__":
    main()
