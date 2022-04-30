
import unittest
from Lab001 import readEmployeeFromJSONFile


class TestLab001(unittest.TestCase):
    def test_Employee(self):
        employee_data = readEmployeeFromJSONFile()
        print(employee_data)
        print(employee_data['name'])
        self.assertEqual(employee_data['name'],
                         "Raj", "Employee Name not matching.")


if __name__ == '__main__':
    unittest.main()
