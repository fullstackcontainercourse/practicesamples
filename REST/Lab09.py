
'''
Problem Statement :
Call the REST API to GET oen particular Employee details and print all the details of the employee in json format.

Approach :
Similar to Lab08 but the URL for GET API will be different.
Complete the code to fetch particular employee data by calling the GET employe by Id API.
Hints:
From Lab08 response, know the Id of any one of the employee.
Pass that id to get employee by ID API to fetch that ID
Use json, requests modules.
Refer RestRef file for code usage & references
'''
import unittest


# Use request module to call a GET REST API for employees

# print the response content

# use json.dumps to convert response into string

# refer reference to convert json string into a python object

# print all employee details
# for example like response._embedded.employees[0].firstName


def getEmployeeById(id):

    # Use request module to call a GET REST API for employees by Id
    # Check the URL to have employee ID passed
     employeeObject = << get Employee by Id >>
    # print the response content

    # use json.dumps to convert response into string

    # refer reference to convert json string into a python object

    # return python object
    return employeeObject


class TestLab09(unittest.TestCase):
    def test_EmployeeById(self):
        employee_data = getEmployeeById(1)
        print(employee_data.firstName)
        self.assertEqual(employee_data.firstName,
                         "Frodo", "Employee First Name not matching.")
        self.assertEqual(employee_data.lastName,
                         "Baggins", "Employee Last Name not matching.")
        self.assertEqual(employee_data.role,
                         "ring bearer", "Employee role Name not matching.")

        employee_data2 = getEmployeeById(2)
        print(employee_data2.firstName)
        self.assertEqual(employee_data2.firstName,
                         "Bilbo", "Employee First Name not matching.")
        self.assertEqual(employee_data2.lastName,
                         "Baggins", "Employee Last Name not matching.")
        self.assertEqual(employee_data2.role,
                         "burglar", "Employee role Name not matching.")


if __name__ == '__main__':
    unittest.main()
