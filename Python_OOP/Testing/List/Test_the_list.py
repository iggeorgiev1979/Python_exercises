from extended_list import IntegerList
from unittest import TestCase, main

class TestList(TestCase):
    def setUp(self):
        self.list = IntegerList(1, 2, 3, 4, 5)
    
    def test_if_the_list_constructor_works(self):
        self.assertEqual([1, 2, 3, 4, 5], self.list._IntegerList__data)
    
    def test_if_constructor_takes_none_integer_values(self):
        some_list = IntegerList("3", "something")
        self.assertEqual([], some_list._IntegerList__data)


    def test_if_value_error_is_thrown_when_try_to_add_none_integer(self):
        with self.assertRaises(ValueError) as er:
            self.list.add("something")    
        self.assertEqual("Element is not Integer", str(er.exception))
    
    def test_add_method(self):
        self.list.add(8)
        self.assertEqual([1, 2, 3, 4, 5, 8], self.list._IntegerList__data)

    def test_if_remove_index_works(self):
        with self.assertRaises(IndexError) as er:
            element = self.list.remove_index(7)
        self.assertEqual("Index is out of range", str(er.exception))
    
    def test_remove_index_method(self):
        element = self.list.remove_index(0)
        self.assertEqual(1,element)
    
    def test_if_get_method_works(self):
        with self.assertRaises(IndexError) as er:
            element = self.list.get(8)
        self.assertEqual("Index is out of range", str(er.exception))
    
    def test_get_method(self):
        element = self.list.get(0)
        self.assertEqual(1, element)
    
    def test_if_insert_method_works(self):
        with self.assertRaises(ValueError) as er:
            self.list.insert(2, 2.5)
        self.assertEqual("Element is not Integer", str(er.exception))

    def test_insert_method(self):
        with self.assertRaises(IndexError) as er:
            self.list.insert(9, 5)
        self.assertEqual("Index is out of range", str(er.exception))
    
    def test_insert_method_with_integer_value(self):
        self.list.insert(1, 9)
        self.assertEqual([1, 9, 2, 3, 4, 5], self.list._IntegerList__data)
    
    def test_the_get_biggest_method(self):
        element = self.list.get_biggest()
        self.assertEqual(5, element)
    
    def test_if_the_get_index_method_works(self):
        index = self.list.get_index(2)
        self.assertEqual(1, index)


if __name__ == "__main__":
    main()
