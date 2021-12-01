import sys
sys.path.append("..")
from project.pet_shop import PetShop
from unittest import TestCase, main

class TestPetShop(TestCase):
    def setUp(self):
        self.shop = PetShop("Zoo")

    def test_constructor(self):
        self.assertEqual("Zoo", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)
    
    def test_add_food(self):
        with self.assertRaises(ValueError) as er:
            self.shop.add_food("some", -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(er.exception))

        with self.assertRaises(ValueError) as er:
            self.shop.add_food("some", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(er.exception))

        msg = self.shop.add_food("some", 10)
        self.assertEqual({"some": 10}, self.shop.food)
        self.assertEqual(10, self.shop.food["some"])
        self.assertEqual('Successfully added 10.00 grams of some.', msg)
    
    def test_add_pet(self):
        msg = self.shop.add_pet("Rick")
        self.assertEqual("Successfully added Rick.", msg)

        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("Rick")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
    
    def test_feed_pet(self):
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("some", "Rick")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))
        
        self.shop.add_pet("Rick")
        msg = self.shop.feed_pet("some", "Rick")
        self.assertEqual('You do not have some', msg)
        self.shop.add_food("some", 80)
        msg = self.shop.feed_pet("some", "Rick")
        self.assertEqual("Adding food...", msg)
        self.assertEqual(1080.00, self.shop.food["some"])
        self.assertEqual({"some": 1080}, self.shop.food)
        msg = self.shop.feed_pet("some", "Rick")
        self.assertEqual("Rick was successfully fed", msg)
        self.assertEqual(980.00, self.shop.food["some"])
        self.assertEqual({"some": 980}, self.shop.food)
    
    def test_repr(self):
        self.shop.add_pet("Rick")
        msg = repr(self.shop)
        self.assertEqual('Shop Zoo:\nPets: Rick', msg)


if __name__ == "__main__":
    main()

