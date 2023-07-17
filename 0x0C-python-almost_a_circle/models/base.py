#!/usr/bin/python3
'''This module has the class Base
'''
import json
import csv
import turtle


class Base:
    '''
    Base class for managing id attribute of future classes
    and to avoid duplicating the same code (by extension, same bugs).

    Attributes:
        __nb_objects (int): Private class attribute to keep track
                            of the number of objects created.
        id (int): Public instance attribute representing the id
                  of an object.

    Methods:
        __init__(self, id=None): Class constructor. Initializes the id
        attribute based on the provided argument or an auto-incremented
        value

    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initializes a Base objec with an id.

        Args:
            id (int, optional): The id value to assign to the object.
                                Defaults to None.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries: A list of dictionaries.
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Writes the JSON string representation of list_objs to a file

        Args:
            cls (type): The class
            list_objs (list): The list of instances.
        '''
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dictionaries = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(dictionaries)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        '''
        Returns the list of the JSON string representation json_string

        Args:
            json_string (str): The string representating a list of
                               dictionaries.
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Returns an instance with all attributes already set

        Args:
            cls: The class.
            **dictionary (dict): The dictionary representing the attributes.

        Returns:
            object: An instance with all attributes already set.
        '''
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = None

        if dummy_instance is not None:
            dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        '''
        Returns a list of instances loaded from a file.

        Args:
            cls (type): The class.

        Returns:
            list: The list of instances loaded from a file.
        '''
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictries = cls.from_json_string(json_string)
                return [cls.create(**dictionary) for dictionary in dictries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        Serializes and save list_objs to CSv file.

        Args:
            cls (type): The class.
            list_objs (list): The list of instances.
        '''
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                writer = csv.writer(file)
                if cls.__name__ == "Rectangle":
                    for o in list_objs:
                        writer.writerow([o.id, o.width, o.height, o.x, o.y])
                elif cls.__name__ == "Square":
                    for o in list_objs:
                        writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        '''
        Deserializes and loads instances from a CSV file.

        Args:
            cls (type): The class

        Returns:
            list: The list of instances loaded  from a CSV file
        '''
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline='') as file:
                if cls.__name__ == "Rectangle":
                    instance = ["id", "width", "height", "x", "y"]
                else:
                    instance = ["id", "size", "x", "y"]
                instances = csv.DictReader(file, fieldnames=instance)
                instances = [dict([k, int(v)] for k, v in d.items())
                             for d in instances]
                return [cls.create(**d) for d in instances]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''
        Opens and draws all the Rectangles and Squares

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.
        '''
        turtle.Screen().bgcolor("white")
        turtle.speed(0)

        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.color("blue")
            for i in range(2):
                turtle.forward(rectangle.width)
                turtle.right(90)
                turtle.forward(rectangle.height)
                turtle.right(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.color("red")
            for i in range(4):
                turtle.forward(square.size)
                turtle.right(90)

        turtle.exitonclick()
