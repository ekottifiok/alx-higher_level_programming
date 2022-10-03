#!/usr/bin/python3
"""Base Module"""


from json import dumps, load, loads


class Base:
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the class instance

        Args:
            id (any, optional): stores the input in a
            public instance attribute. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list or dict): the data to be converted to json

        Returns:
            str: a json file
        """
        if list_dictionaries is None:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): the list of
        """
        list_objs_list = []
        with open(f"{cls.__name__}.json", "w") as file:
            for r in list_objs:
                list_objs_list.append(r.to_dictionary())
            file.write(cls.to_json_string(list_objs_list))

    @classmethod
    def load_from_file(cls):
        with open(f"{cls.__name__}.json", 'r') as file:
            return load(file)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves data to a csv file

        Args:
            list_objs (list): contains the list of objects
            to be saved in a file
        """
        list_objs_list = []

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a new instance of the class

        Returns:
            class: dummy class instance
        """
        dummy = None
        if cls.__name__ == "Square":
            dummy = cls(dictionary["size"])
        elif cls.__name__ == "Rectangle":
            dummy = cls(dictionary["width"], dictionary["height"])
        dummy.update(**dictionary)
        return dummy
