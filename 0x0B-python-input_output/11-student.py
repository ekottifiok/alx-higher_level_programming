#!/usr/bin/python3
"""Student module"""


class Student:
    """the class instance for the Student
    """

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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        Args:
            attrs (str, optional): attributes to look for. Defaults to None.

        Returns:
            dict: attributes found
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        dict_re = {}
        for i in attrs:
            try:
                dict_re[i] = self.__dict__[i]
            except (KeyError,):
                pass
        return dict_re

    def reload_from_json(self, json):
        """replaces the values found in the dict

        Args:
            json (dict): attributes to be replaced
        """
        for key, value in json.items():
            setattr(self, key, value)
