import unittest
import json
from Lab002 import getStudentDataAsJson


class TestLab002(unittest.TestCase):
    def test_Student_as_json(self):
        student_data_asJson = getStudentDataAsJson()
        print(student_data_asJson)
        student_as_dict = json.loads(student_data_asJson)
        self.assertEqual(student_as_dict['name'],
                         "Gil", "Student Name not matching.")
        self.assertEqual(student_as_dict['age'],
                         20, "Student Age not matching.")
        self.assertEqual(len(student_as_dict['subjects']),
                         4, "Student Subjects list size not matching.")


if __name__ == '__main__':
    unittest.main()
