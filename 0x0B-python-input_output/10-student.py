#!/usr/bin/python3
'''Has a class Student that defines a student by:(based on 9-student.py).
'''


class Student:
    '''
    Class representing a student.
    '''
    def __init__(self, first_name, last_name, age):
        '''
        Initialize a Student instance with first name, last name and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Retrieve a dictiionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.
                                    If None, retrieve all attributes.

        Returns:
            dict: The dictionary representation of the Student instance.
        '''
        if attrs is None:
            return self.__dict__
        json_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                json_dict[attr] = self.__dict__[attr]
        return json_dict
