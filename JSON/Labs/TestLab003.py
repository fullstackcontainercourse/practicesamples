
import unittest
from Lab003 import readEmployeeFromJSONFile


class TestLab003(unittest.TestCase):
    def test_Employee(self):
        employee_data = readEmployeeFromJSONFile()
        print(employee_data['manager'])
        self.assertEqual(employee_data['name'],
                         "Raj", "Employee Name not matching.")
        self.assertEqual(employee_data['age'],
                         30, "Employee Age not matching.")
        self.assertEqual(employee_data['dept'],
                         "IT", "Employee Age not matching.")
        self.assertEqual(employee_data['manager'],
                         "Alice", "Employee Manager name not matching.")
        self.assertEqual(employee_data['yearsofexp'],
                         5, "Employee YearsOfExp name not matching.")


if __name__ == '__main__':
    unittest.main()
