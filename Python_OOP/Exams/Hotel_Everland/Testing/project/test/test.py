import sys
sys.path.append("..")
from project.student_report_card import StudentReportCard
from unittest import TestCase, main

class TestCard(TestCase):
    def setUp(self):
        self.card = StudentReportCard("Ivan", 10)
    
    def test_constructor(self):
        with self.assertRaises(ValueError) as er:
            card = StudentReportCard("", 10)
        self.assertEqual("Student Name cannot be an empty string!", str(er.exception))

        with self.assertRaises(ValueError) as er:
            card = StudentReportCard("Ivan", 0)
        self.assertEqual("School Year must be between 1 and 12!", str(er.exception))

        with self.assertRaises(ValueError) as er:
            card = StudentReportCard("Ivan", 13)
        self.assertEqual("School Year must be between 1 and 12!", str(er.exception))

        self.assertEqual("Ivan", self.card.student_name)
        self.assertEqual(10, self.card.school_year)
        self.assertEqual({}, self.card.grades_by_subject)
    
    def test_add_grade(self):
        self.card.add_grade("math", 4)
        self.assertEqual({"math": [4]}, self.card.grades_by_subject)
        self.assertEqual([4], self.card.grades_by_subject["math"])
        self.card.add_grade("math", 5)
        self.card.add_grade("bio", 5)
        msg = self.card.average_grade_by_subject()
        self.assertEqual("math: 4.50\nbio: 5.00", msg)

    def test_average_grade(self):
        self.card.add_grade("math", 4)
        self.card.add_grade("bio", 5)
        msg = self.card.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 4.50", msg)

    def test_repr(self):
        self.card.add_grade("math", 4)
        self.card.add_grade("bio", 5)
        msg = self.card.__repr__()
        expected_msg = f"Name: Ivan\n" \
                 f"Year: 10\n" \
                 f"----------\n" \
                 f"math: 4.00\n" \
                 f"bio: 5.00\n" \
                 f"----------\n" \
                 f"Average Grade: 4.50"



if __name__ == "__main__":
    main()

