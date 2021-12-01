import sys
sys.path.append("..")
from project.library import Library
from unittest import TestCase, main

class TestLibrary(TestCase):
    def setUp(self):
        self.test_library = Library("Central")
    
    def test_the_valid_name(self):
        self.assertEqual("Central", self.test_library.name)
    
    def test_not_valid_name(self):
        
        with self.assertRaises(ValueError) as er:
            ll = Library("")
        
        self.assertEqual("Name cannot be empty string!", str(er.exception))
    
    def test_add_book(self):
        self.test_library.add_book(author="King", title="IT")
        self.assertEqual({"King":["IT"]}, self.test_library.books_by_authors)
        self.assertEqual(["IT"], self.test_library.books_by_authors["King"])
    
    def test_add_reader(self):
        self.test_library.add_reader("Ivan")
        self.assertEqual({"Ivan": []}, self.test_library.readers)
        msg = self.test_library.add_reader("Ivan")
        self.assertEqual("Ivan is already registered in the Central library.", msg)
    
    def test_rent_book(self):
        msg = self.test_library.rent_book(reader_name="Ivan", book_author="King", book_title="IT")
        self.assertEqual("Ivan is not registered in the Central Library.", msg)
        self.test_library.add_reader("Ivan")
        msg = self.test_library.rent_book(reader_name="Ivan", book_author="King", book_title="IT")
        self.assertEqual("Central Library does not have any King's books.", msg)
        self.test_library.add_book("King", "IT")
        msg = self.test_library.rent_book("Ivan", "King", "Kelly")
        self.assertEqual("""Central Library does not have King's "Kelly".""", msg)
        self.test_library.rent_book("Ivan", "King", "IT")
        self.assertEqual({"Ivan": [{"King": "IT"}]}, self.test_library.readers)
        self.assertEqual([{"King": "IT"}], self.test_library.readers["Ivan"])
        self.assertEqual({"King": "IT"}, self.test_library.readers["Ivan"][0])
        self.assertEqual("IT", self.test_library.readers["Ivan"][0]["King"])
        self.assertEqual([], self.test_library.books_by_authors["King"])



if __name__ == "__main__":
    main()
