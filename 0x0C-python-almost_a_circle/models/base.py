#!/usr/bin/python3
"""
A model that contains a Base class to manage
the id attribute of all classes that extend
from Base and avoid duplicate the same code.
"""

from csv import DictWriter, reader
from os import path
from json import loads, dumps
from turtle import begin_fill, color, done, down, \
    end_fill, forward, home, left, setpos, up, write


class Base:
    """
    ...
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        ...
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): the list of
        """
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for elem in list_objs:
                json_attrs.append(elem.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation

        Args:
            json_string (str): the string in json

        Returns:
            str: string converted
        """
        if json_string is None or len(json_string) == 0:
            return []

        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a new instance of the class

        Returns:
            class: dummy class instance
        """
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """that returns a list of instances

        Returns:
            list: of new instances read from a file
        """
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            instances = []

            for elem in objs:
                instances.append(cls.create(**elem))

            return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves data to a csv file

        Args:
            list_objs (list): contains the list of objects
            to be saved in a file
        """
        class_name = cls.__name__
        with open(f"{class_name}.csv", 'w') as file:
            if class_name == "Rectangle":
                arr = ["id", "width", "height", "x", "y"]
            elif class_name == "Square":
                arr = ["id", "size", "x", "y"]
            else:
                return
            csv_writer = DictWriter(file, fieldnames=arr)
            for r in list_objs:
                csv_writer.writerow(r.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """reads from a csv file

        Returns:
            class: the class to look for
        """
        class_name = cls.__name__

        result_arr = []
        try:
            with open(f"{class_name}.csv", 'r') as file:
                if class_name == "Rectangle":
                    arr = ["id", "width", "height", "x", "y"]
                elif class_name == "Square":
                    arr = ["id", "size", "x", "y"]
                else:
                    return
                csv_reader = reader(file)
                for row in csv_reader:
                    result_arr.append(cls.create(
                        **({arr[i]: int(row[i]) for i in range(len(row))})))
            return result_arr
        except (FileNotFoundError,):
            return result_arr

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation

        Args:
            json_string (str): the string in json

        Returns:
            str: string converted
        """
        if json_string is None:
            return "[]"
        return loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """applies a turtle implementation of the instance

        Args:
            list_rectangles (_type_): _description_
            list_squares (_type_): _description_
        """
        if len(list_squares) == 0 and len(list_rectangles) == 0:
            return

        if list_rectangles is not []:
            color('red', 'yellow')
            for obj in list_rectangles:
                down()
                write("Rectangle", align="right")
                begin_fill()
                forward(obj.width)
                left(90)
                forward(obj.height)
                left(90)
                forward(obj.width)
                left(90)
                forward(obj.height)
                left(90)
                end_fill()
                up()
                forward(obj.width+50)

        if list_squares is not []:
            color('blue', 'green')
            home()
            setpos((0, 200))
            forward(obj.width*2)
            for obj in list_squares:
                down()
                write("Square", align="right")
                begin_fill()
                forward(obj.width)
                left(90)
                forward(obj.height)
                left(90)
                forward(obj.width)
                left(90)
                forward(obj.height)
                left(90)
                end_fill()
                up()
                forward(obj.width+50)
        done()
