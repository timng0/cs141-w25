"""
Lecture 17

Last class:
    More on classes
        Hiding information
        Dunder methods
        Modeling

Today:
    More modeling with classes
"""

import csv

class Student:
    """
    Representation of a student at a university
    """
    def __init__(self, name, cnetid, ucid):
        """
        Input:
            name (str): full name for the student
        """
        assert isinstance(name, str)
        assert isinstance(ucid, int)
        self.name = name
        self.institution = 'University of Chicago'
        self.id_number = ucid
        self.email = cnetid + '@uchicago.edu'
        self.courses = []
        self.credits = 0


    def get_cnetid(self):
        """
        Retrieve the CNetID for the student

        Output (str): the CNetID
        """
        cnet = self.email.removesuffix('@uchicago.edu')
        return cnet

    def enroll(self, course):
        assert self.credits + course.get_units() <= 400
        self.courses.append(course)
        self.credits += course.get_units()

    def __repr__(self):
        return f'Student({self.name}, {self.institution}, {self.id_number}, {self.get_cnetid()}, {self.courses}, {self.credits})'

class Course:
    def __init__(self, name, number, dept, units):
        self.__name = name
        self.__number = number
        self.__dept = dept
        self.__units = units

    def get_units(self):
        return self.__units

    def __repr__(self):
        return f'Course({self.__name}, {self.__number}, {self.__dept}, {self.__units})'


def read_stations():
    stations = []
    with open('divvy-stations-20191231.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stations.append(row)
    return stations

def read_trips():
    trips = []
    with open('divvy-trips-20191231.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            trips.append(row)
    return trips
    