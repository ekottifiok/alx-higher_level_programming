#!/usr/bin/python3
"""
A model that contains a Base class to manage
the id attribute of all classes that extend
from Base and avoid duplicate the same code.
"""

from os import path
import json
from turtle import begin_fill, clear, color, delay, done, down, end_fill, forward, home, left, onclick, pos, setpos, setposition, setx, up, write


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
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
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            instances = []

            for elem in objs:
                instances.append(cls.create(**elem))

            return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        def draw_square_rectangle(obj):
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

        color('red', 'yellow')

        if list_rectangles is not []:
            for items in list_rectangles:
                down()
                write("Rectangle", align="right")
                draw_square_rectangle(items)
                up()
                forward(items.width+50)

        color('blue', 'green')
        home()
        setpos((0, 200))
        forward(items.width*2)
        if list_squares is not []:
            for items in list_squares:
                down()
                write("Square", align="right")
                draw_square_rectangle(items)
                up()
                forward(items.width+50)
        done()
