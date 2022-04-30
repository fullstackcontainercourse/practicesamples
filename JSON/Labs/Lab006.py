## Topic : JSON
# Exercise 006

""" 
Problem Statement : 
Read data from Employee json and create an Employee object.(NOT dictionary)


Approach :
Complete the following program and make sure the test cases in TestLab006.py passes successfully/

"""

import json


class Employee(object):
    def __init__(self, name, dept, id, age):
        self.id = id
        self.name = name
        self.dept = dept
        self.age = age


def readEmployeeFromJSONFile():

    return empObject
