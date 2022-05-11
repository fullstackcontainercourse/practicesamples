
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


def createEmployee(firstName, lastName, role):

    return newEmployeeObject


class TestLab10(unittest.TestCase):

    def test_createEmployee(self):
        employee_data = createEmployee('hai', 'hello', 'tester')
        print(employee_data)
        print(employee_data.firstName)
        self.assertEqual(employee_data.firstName, "hai",
                         "Employee First Name not matching.")
        self.assertEqual(employee_data.lastName, "hello",
                         "Employee Last Name not matching.")
        self.assertEqual(employee_data.role, "tester",
                         "Employee Role Name not matching.")


if __name__ == '__main__':
    unittest.main()
