#!/usr/bin/python3
"""A base clase for the Rectangle and Square objects"""
import json
import os.path
import csv


class Base:
    """
    A base class for Rectangle and Square objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """A class constructor for the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A method that returns JSON string
        representation of list_dictionaries
        Arguments:
            list_dictionaries (list): the dictionaries to parse
        Returns:
            str: the json string representation of the list of dicts
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """A method that returns a list of
        JSON string representation

        Arguments:
            json_string (str): string representation of list of dicts

        Returns:
            list: JSON string representation of the json string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """A method that returns an instance with all attributes already set

        Arguments:
            dictionary: double pointer to a dictionary
            cls: any class

        A dummy instance is created before updating it with the provided
        values to avoid errors of None attributes

        Returns:
            dummy (list): a class instance with all attributes set
        """
        if cls.__name__ == "Rectangle":
            dummyinstnce = cls(1, 1)
        if cls.__name__ == "Square":
            dummyinstnce = cls(1)
        dummyinstnce.update(**dictionary)

        return (dummyinstnce)

    @classmethod
    def load_from_file(cls):
        """A method that returns a list of instances

        Arguments:
            cls: any class

        Returns:
            list: a list of all instances
        """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_string = f.read()

        list_class = cls.from_json_string(list_string)
        the_list = []

        for index in range(len(list_class)):
            the_list.append(cls.create(**list_class[index]))

        return the_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """A method that serializes a list of rectangles or squares
        into a csv file

        Arguments:
            cls: any class
            list_objs (list): the list of objects
        """
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline="") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for i in list_objs:
                    writer.writerow([i.id, i.width, i.height, i.x, i.y])
            elif cls.__name__ == "Square":
                for i in list_objs:
                    writer.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """A method that deserializes a list of rectangles or squares
        in a csv file

        Arguments:
            cls: any class
        """
        filename = cls.__name__ + ".csv"
        my_obj = []
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f)
                for elm in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(elm[0]), "width": int(elm[1]),
                                      "height": int(elm[2]), "x": int(elm[3]),
                                      "y": int(elm[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(elm[0]), "size": int(elm[1]),
                                      "x": int(elm[2]), "y": int(elm[3])}
                    obj = cls.create(**dictionary)
                    my_obj.append(obj)
        except (Exception):
            pass
        return (my_obj)

    @classmethod
    def save_to_file(cls, list_objs):
        """A method that writes a JSON string representation of list_objs
        to a file

        Arguments:
            list_objs (list): the list instances that inherits from Base class
        """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)
