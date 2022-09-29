#!/usr/bin/python3
"""Student module"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initializes the dict instance

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age of the instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance

        Returns:
            dict: representation of the instance
        """
        return self.__dict__
