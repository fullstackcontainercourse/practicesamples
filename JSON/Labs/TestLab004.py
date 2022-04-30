
import unittest
from Lab004 import readEmployeeFromJSONFile


class TestLab004(unittest.TestCase):
    def test_Employee(self):
        employee_data = readEmployeeFromJSONFile()
        print(employee_data['name'])
        self.assertEqual(employee_data['name'],
                         "Raj", "Employee Name not matching.")
        self.assertEqual(employee_data['age'],
                         30, "Employee Age not matching.")
        self.assertEqual(employee_data['dept'],
                         "IT", "Employee Age not matching.")
        self.assertIsNotNone(
            employee_data['project'], "Employee doesnt have project object ")
        self.assertEqual(
            employee_data['project']['name'], "Login Module", "Employee project.name doesnt match ")
        self.assertEqual(
            employee_data['project']['tenure'], 3, "Employee project.tenure doesnt match ")


if __name__ == '__main__':
    unittest.main()
