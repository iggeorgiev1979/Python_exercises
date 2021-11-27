import sys
sys.path.append(".")
from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student(name="Ivan")
    
    def test_constructor(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual({}, self.student.courses)
        student = Student("Ivan", {"course_name": ["notes"]})
        self.assertEqual({"course_name": ["notes"]}, student.courses)
    
    def test_enroll_method(self):
        self.student.courses = {"course_name": []}
        msg = self.student.enroll("course_name", ["a", "b"])
        self.assertEqual("Course already added. Notes have been updated.", msg)
        self.assertEqual({"course_name": ["a", "b"]}, self.student.courses)

        self.student.courses = {}
        msg =self.student.enroll("course_name", ["a"])
        self.assertEqual("Course and course notes have been added.", msg)
        self.assertEqual({"course_name": ["a"]}, self.student.courses)


        self.student.courses = {}
        msg =self.student.enroll("course_name", ["a"], "Y")
        self.assertEqual("Course and course notes have been added.", msg)
        self.assertEqual({"course_name": ["a"]}, self.student.courses)


        self.student.courses = {}
        msg = self.student.enroll("course_name", ["a"], "no")
        self.assertEqual("Course has been added.", msg)
        self.assertEqual({"course_name": []},self.student.courses)

    def test_add_notes_method(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("course_name", ["a", "b"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

        self.student.courses = {"course_name": []}
        msg = self.student.add_notes("course_name", ["a", "b"])
        self.assertEqual("Notes have been updated", msg)
        self.assertEqual({"course_name": [["a", "b"]]}, self.student.courses)

    def test_leave_course_method(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("course_name")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

        self.student.courses = {"course_name": []}
        msg = self.student.leave_course("course_name")
        self.assertEqual("Course has been removed", msg)
        self.assertEqual({}, self.student.courses)

if __name__ == "__main__":
    main()

